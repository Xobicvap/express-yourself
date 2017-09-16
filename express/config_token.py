from tokentypes import TokenType
from token import Token

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
