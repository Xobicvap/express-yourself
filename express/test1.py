from parser import Parser
from token import Token
from tokentypes import TokenType
from parselets import *
from node import print_tree
from var_repo import VarRepo
from precedence import Precedence

t1 = Token(TokenType.VARIABLE, 'A')
t2 = Token(TokenType.ASSIGNMENT, '=')
t3 = Token(TokenType.NUMERIC, '5')

t4 = Token(TokenType.VARIABLE, 'B')
t5 = Token(TokenType.ASSIGNMENT, '=')
t6 = Token(TokenType.VARIABLE, 'A')
t7 = Token(TokenType.PLUS, '+')
t8 = Token(TokenType.NUMERIC, '1')

p = Parser([t1, t2, t3])

p.register(TokenType.VARIABLE, VariableParselet())
p.register(TokenType.ASSIGNMENT, AssignParselet())
p.register(TokenType.NUMERIC, NumericParselet())

n = p.parseExpression()
print_tree(n)

vr = VarRepo()
r = n.evaluate(vr)
print vr.repo


print("\n\n\n")
p2 = Parser([t4, t5, t6, t7, t8])

p2.register(TokenType.VARIABLE, VariableParselet())
p2.register(TokenType.ASSIGNMENT, AssignParselet())
p2.register(TokenType.NUMERIC, NumericParselet())
p2.register(TokenType.PLUS, BinaryOperatorParselet(Precedence.SUM, False))

n = p2.parseExpression()
print_tree(n)

r = n.evaluate(vr)
print vr.repo
