from node import Node
from variable import Variable
from precedence import Precedence

class PrefixParselet:
  def parse(self, parser, token):
    raise Exception("Not implemented")

class InfixParselet:
  def parse(self, parser, left, token):
    raise Exception("Not implemented")

class VariableParselet(PrefixParselet):
  def parse(self, parser, token):
    return Node(Variable(token.getValue()))

class AssignParselet(InfixParselet):
  def getPrecedence(self):
    return Precedence.ASSIGNMENT

  def parse(self, parser, left, token):
    right = parser.parseExpression(0)
    return Node(token.getValue(), left, right)

class NumericParselet(PrefixParselet):
  def parse(self, parser, token):
    v = token.getValue()
    try:
      return Node(int(v))
    except ValueError:
      return Node(float(v))

class BinaryOperatorParselet(InfixParselet):
  def __init__(self, precedence, isRight):
    self.precedence = precedence
    self.isRight = isRight

  def getPrecedence(self):
    return self.precedence

  def parse(self, parser, left, token):
    useRight = 1 if self.isRight else 0
    right = parser.parseExpression(self.precedence - useRight)
    return Node(token.getValue(), left, right)


