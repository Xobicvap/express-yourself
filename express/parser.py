from parselets import PrefixParselet, InfixParselet

class Parser:

  def __init__(self):
    self.prefix_parselets = {}
    self.infix_parselets = {}
    self.reads = []

  def token_define(self, tokens):
    if type(tokens) is not list:
      raise Exception("Must provide list of tokens to parser")
    self.tokens = tokens
    self.token_iter = iter(tokens)    

  def register(self, tokentype, parselet):
    # code smell- don't use isinstance, maybe ensure types
    # via another means?
    if isinstance(parselet, PrefixParselet):
      self.prefix_parselets[tokentype] = parselet
    elif isinstance(parselet, InfixParselet):
      self.infix_parselets[tokentype] = parselet

  def lookAhead(self, distance):
    while distance >= len(self.reads):
      try:
        self.reads.append(self.token_iter.next())
      except StopIteration:
        break
    if len(self.reads) > 0:
      return self.reads[distance]
    return None

  def consume(self):
    self.lookAhead(0)
    return self.reads.pop(0)

  def getPrecedence(self):
    t = self.lookAhead(0)
    if t is not None:
      parselet = self.infix_parselets[self.lookAhead(0).getType()]
      if parselet is not None:
        return parselet.getPrecedence()
    return 0

  def match(self, expected):
    token = self.lookAhead(0)
    if token.getType() != expected:
      return False

    self.consume()
    return True

  def parseExpression(self, precedence = 0):
    token = self.consume()
    # raise KeyError instead?
    prefix_parselet = self.prefix_parselets[token.getType()]
    if prefix_parselet == None:
      raise Exception("Could not parse \"" + token + "\".")

    left = prefix_parselet.parse(self, token)
    while precedence < self.getPrecedence():
      token = self.consume()
      infix_parselet = self.infix_parselets[token.getType()]
      left = infix_parselet.parse(self, left, token)

    return left

