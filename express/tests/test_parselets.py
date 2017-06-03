from node import Node
from parselets import *
from token import Token
from tokentypes import TokenType
from variable import Variable
import unittest

class ParseletTest(unittest.TestCase):

  def testVariableParselet(self):
    vp = VariableParselet()
    n = vp.parse(None, Token(TokenType.VARIABLE, "Foo"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, Variable)
    self.assertEqual("Foo", str(n.value))

  def testNumericParseletWithIntValue(self):
    np = NumericParselet()
    n = np.parse(None, Token(TokenType.NUMERIC, "9000"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, int)
    self.assertEqual(n.value, 9000)

  def testNumericParseletWithFloatValue(self):
    np = NumericParselet()
    n = np.parse(None, Token(TokenType.NUMERIC, "3.14"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, float)
    self.assertEqual(n.value, 3.14)
