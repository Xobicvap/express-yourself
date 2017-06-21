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

  def testNumericParseletWithNonNumeric(self):
    np = NumericParselet()
    with(self.assertRaises(Exception)):
      np.parse(None, Token(TokenType.NUMERIC, "abcdefg"))

  def testStringParseletWithNonString(self):
    sp = StringParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.STRING, 31.4))

  def testStringParseletWithStringNoQuoteBounds(self):
    sp = StringParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.STRING, "abcdefg"))
#    self.assertRaises(Exception, sp.parse(None, Token(TokenType.STRING, "abcdefg")))

  def testStringParseletWithStringValue(self):
    sp = StringParselet()
    n = sp.parse(None, Token(TokenType.STRING, "\"hello\""))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, basestring)
    self.assertEqual(n.value, "hello")

  def testSetParseletWithNonset(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)): 
      sp.parse(None, Token(TokenType.SET, "(a, b, c)"))
      sp.parse(None, Token(TokenType.SET, "a, b, c"))
      sp.parse(None, Token(TokenType.SET, "[a, b, c"))
      sp.parse(None, Token(TokenType.SET, "a, b, c]"))
      sp.parse(None, Token(TokenType.SET, "<a, b, c>"))

  def testSetParseletWithNestedSet(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a, b, [c,d]]"))

  def testSetParseletWithNestedMap(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a, {b: c}, d]"))

  def testSetParseletWithNonCommaDelimited(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a b c]"))
      sp.parse(None, Token(TokenType.SET, "[a | b | c]"))
      sp.parse(None, Token(TokenType.SET, "[a; b; c]"))

  def testSetParseletWithDuplicates(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a, b, c, a]"))

  def testSetParseletWithSet(self):
    sp = SetParselet()
    n = sp.parse(None, Token(TokenType.SET, "[a, b, c]"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, list)
    self.assertEquals(len(n.value), 3)
    self.assertIn('a', n.value)
    self.assertIn('b', n.value)
    self.assertIn('c', n.value)

  def testMapParseletWithNonmap(self):
    mp = MapParselet()
    with(self.assertRaises(Exception)):
      mp.parse(None, Token(TokenType.MAP, "(a, b, c)"))
      mp.parse(None, Token(TokenType.MAP, "a, b, c"))
      mp.parse(None, Token(TokenType.MAP, "{a, b, c"))
      mp.parse(None, Token(TokenType.MAP, "a, b, c}"))
      mp.parse(None, Token(TokenType.MAP, "<a, b, c>"))

