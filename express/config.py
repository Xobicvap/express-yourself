from operators import *
from tokentypes import TokenType
from token import Token
from parselets import *

token_defs = [
  (r"([A-Za-z]+)", lambda scanner, token: Token(TokenType.VARIABLE, token)),
  (r"([0-9]+)", lambda scanner, token: Token(TokenType.NUMERIC, token)),
  (r"\?\.\.", lambda scanner, token: Token(TokenType.RANDRANGE, token)),
  (r"\=", lambda scanner, token: Token(TokenType.ASSIGNMENT, token)),
  (r"\+", lambda scanner, token: Token(TokenType.PLUS, token)),
  (r"\-", lambda scanner, token: Token(TokenType.MINUS, token)),
  (r"\*", lambda scanner, token: Token(TokenType.ASTERISK, token)),
  (r"\/", lambda scanner, token: Token(TokenType.SLASH, token)),
  (r".", lambda scanner, token: None)
]

operator_map = {
  "=" : AssignOperator(),
  "+" : AddOperator(),
  "-" : SubtractOperator(),
  "*" : MultiplyOperator(),
  "/" : DivisionOperator(),
  "?..": RandrangeOperator()
}

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

