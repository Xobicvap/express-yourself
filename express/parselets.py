from node import Node
from variable import Variable
from precedence import Precedence
import parseutils

class PrefixParselet:
  """ Base class for prefix tokens, i.e. those that begin a line or expression.
  """
  def parse(self, parser, token):
    """ Not implemented in the base class.
    """
    raise Exception("Not implemented")

class InfixParselet:
  """ Base class for infix tokens, i.e. those within a line or expression.
  """
  def parse(self, parser, left, token):
    """ Not implemented in the base class.
    """
    raise Exception("Not implemented")

class PostfixParselet:
  """ Base class for postfix tokens.
  """
  def parse(self, parser, left, token):
    """ Not implemented in the base class.
    """
    raise Exception("Not implemented")

class VariableParselet(PrefixParselet):
  """ Parselet for parsing variables. 
      
      This doesn't *assign* variables. That's operators you're thinking of.
      This is more like a variable declaration.
  """
  def parse(self, parser, token):
    """ Transforms the token value into a node containing a Variable.

        Arguments:
          parser (Parser): parser instance, not used here
          token (str): token instance
    """
    return Node(Variable(token.get_value()))

class AssignParselet(InfixParselet):
  """ Assigns the value on the right side to the value on the left.
  """
  def get_precedence(self):
    """ Assignment takes precedence over most things.
    """
    return Precedence.ASSIGNMENT

  def parse(self, parser, left, token):
    """ Creates a node whose left node is the variable being assigned
        and whose right node is the value being assigned.

        Arguments:
          parser (Parser): parser instance
          left (Node): node to assign value to
          token (Token): (assignment) operator token
    """
    right = parser.parse_expression(0)
    return Node(token.get_value(), left, right)

class NumericParselet(PrefixParselet):
  """ Represents a numeric value.
  """
  def parse(self, parser, token):
    """ Transforms the token value into a node containing a numeric value.

        Arguments:
          parser (Parser): parser instance, not used here
          token (str): token instance
    """
    v = token.get_value()
    parseutils.validate_numeric(v)
    try:
      return Node(int(v))
    except ValueError:
      return Node(float(v))

class StringParselet(PrefixParselet):
  """ Represents a string value.
  """
  def parse(self, parser, token):
    """ Transforms the token value into a node containing a string value.

        Arguments:
          parser (Parser): parser instance, not used here
          token (str): token instance
    """
    v = token.get_value()
    parseutils.validate_string(v)
    removed = parseutils.remove_chars(v, "\"")
    return Node(removed)

class SetParselet(PrefixParselet):
  """ Represents a set. Sets cannot have duplicate values.
  """
  def parse(self, parser, token):
    """ Transforms the token value into a node containing a set value.

        Arguments:
          parser (Parser): parser instance, not used here
          token (str): token instance
    """
    v = token.get_value()
    strset = parseutils.set_parse(v)
    return Node(strset)

class MapParselet(PrefixParselet):
  """ Represents a map (dict in Python parlance)
  """
  def parse(self, parser, token):
    """ Transforms the token value into a node containing a map value.

        Arguments:
          parser (Parser): parser instance, not used here
          token (str): token instance
    """
    v = token.get_value()
    strmap = parseutils.map_parse(v)
    return Node(strmap)

class BinaryOperatorParselet(InfixParselet):
  """ Parselet used for binary operators like + - * / etc.
  """
  def __init__(self, precedence, isRight):
    self.precedence = precedence
    self.isRight = isRight

  def get_precedence(self):
    return self.precedence

  def parse(self, parser, left, token):
    useRight = 1 if self.isRight else 0
    right = parser.parse_expression(self.precedence - useRight)
    return Node(token.get_value(), left, right)

class UnaryPostfixOperatorParselet(PostfixParselet):
  def __init__(self, precedence):
    self.precedence = precedence

  def get_precedence(self):
    return self.precedence

  def parse(self, parser, left, token):
    return Node(token.get_value(), left)

class UnaryPrefixOperatorParselet(PrefixParselet):
  def __init__(self, precedence):
    self.precedence = precedence

  def get_precedence(self):
    return self.precedence

  def parse(self, parser, token):
    left = parser.parse_expression(self.precedence)
    return Node(token.get_value(), left)





