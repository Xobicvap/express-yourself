from parselets import PrefixParselet, InfixParselet

class Parser:
  """ Class that does the dirty work of parsing a text-based expression into
      an expression tree. It's a Pratt / top-down operator precedence parser,
      if this sort of thing interests you.

      Attributes:
        prefix_parselets (dict): Map of token types to prefix parselets
        infix_parselets (dict): Map of token types to infix parselets
        reads (list): list of tokens read
  """
  def __init__(self):
    self.prefix_parselets = {}
    self.infix_parselets = {}
    self.reads = []

  def token_define(self, tokens):
    """ Method that sets the tokens readable by this parser, and creates
        an iterator to walk through them.

        Arguments:
          tokens (list): list of readable tokens
    """
    if type(tokens) is not list:
      raise Exception("Must provide list of tokens to parser")
    self.tokens = tokens
    self.token_iter = iter(tokens)    

  def register(self, tokentype, parselet):
    """ Registers a parselet with a token type.
        PrefixParselets are those that begin an expression;
        InfixParselets occur at any other position in the expression.

        Arguments:
          tokentype (TokenType): the type to register with the parselet
          parselet (Parselet): the parselet to register with this type
    """
    if hasattr(parselet, "__name__"):
      """
      this is needed because of a unit test weirdness
      it seems to be passing in the class, not the instance
      - but only during the test? idk, fix later
      """
      parselet = parselet()
    if isinstance(parselet, PrefixParselet):
      self.prefix_parselets[tokentype] = parselet
    elif isinstance(parselet, InfixParselet):
      self.infix_parselets[tokentype] = parselet
    else:
      raise Exception("Did not understand parselet type: " + parselet_type)

  def look_ahead(self, distance):
    """ Pushes a token to stack if distance is greater than the stack length.
        Returns the distance-th item in the token stack, or None if
        there are no items in the stack.

        Arguments:
          distance (int): distance to read in the stack
    """
    while distance >= len(self.reads):
      try:
        self.reads.append(self.token_iter.next())
      except StopIteration:
        break
    if len(self.reads) > 0:
      return self.reads[distance]
    return None

  def consume(self):
    """ Pops the next token in the stack.
    """
    self.look_ahead(0)
    return self.reads.pop(0)

  def get_precedence(self):
    """ Gets the precedence of the next infix parselet.
    """
    t = self.look_ahead(0)
    if t is not None:
      parselet = self.infix_parselets[self.look_ahead(0).get_type()]
      if parselet is not None:
        return parselet.get_precedence()
    return 0

  def match(self, expected):
    """ Gets the next token in the stack and compares it against the
        expected token type. If successful, pops off this token
        and returns True.

        Arguments:
          expected (TokenType): expected token type
    """
    token = self.look_ahead(0)
    if token.get_type() != expected:
      return False

    self.consume()
    return True

  def parse_expression(self, precedence = 0):
    """ Parses an expression. Gets the first token as a PrefixParselet,
        then gets the next token(s) as InfixParselets until finished.

        Arguments:
          precedence (int): expected precedence of this part of the expression
    """
    token = self.consume()
    # raise KeyError instead?
    prefix_parselet = self.prefix_parselets[token.get_type()]
    if prefix_parselet == None:
      raise Exception("Could not parse \"" + token + "\".")

    left = prefix_parselet.parse(self, token)
    while precedence < self.get_precedence():
      token = self.consume()
      infix_parselet = self.infix_parselets[token.get_type()]
      left = infix_parselet.parse(self, left, token)

    return left

