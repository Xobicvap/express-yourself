from parselets import *
from tokentypes import *

parselet_map = {
  TokenType.VARIABLE: VariableParselet(),
  TokenType.ASSIGNMENT: AssignParselet(),
  TokenType.NUMERIC: NumericParselet(),
  TokenType.STRING: StringParselet(),
  TokenType.SET: SetParselet(),
  TokenType.MAP: MapParselet(),
  TokenType.PLUS: BinaryOperatorParselet(Precedence.SUM, False),
  TokenType.MINUS: BinaryOperatorParselet(Precedence.DIFFERENCE, False),
  TokenType.ASTERISK: BinaryOperatorParselet(Precedence.PRODUCT, False),
  TokenType.SLASH: BinaryOperatorParselet(Precedence.DIVISION, False),
  TokenType.RANDRANGE: BinaryOperatorParselet(Precedence.RANDRANGE, False)
}
