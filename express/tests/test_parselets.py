from node import Node
from parselets import *
from token import Token
from tokentypes import TokenType
from variable import Variable
import unittest

class ParseletTest(unittest.TestCase):

  def test_variable_parselet(self):
    vp = VariableParselet()
    n = vp.parse(None, Token(TokenType.VARIABLE, "Foo"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, Variable)
    self.assertEqual("Foo", str(n.value))

  def test_numeric_parselet_with_int_value(self):
    np = NumericParselet()
    n = np.parse(None, Token(TokenType.NUMERIC, "9000"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, int)
    self.assertEqual(n.value, 9000)

  def test_numeric_parselet_with_float_value(self):
    np = NumericParselet()
    n = np.parse(None, Token(TokenType.NUMERIC, "3.14"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, float)
    self.assertEqual(n.value, 3.14)

  def test_numeric_parselet_with_non_numeric(self):
    np = NumericParselet()
    with(self.assertRaises(Exception)):
      np.parse(None, Token(TokenType.NUMERIC, "abcdefg"))

  def test_string_parselet_with_non_string(self):
    sp = StringParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.STRING, 31.4))

  def test_string_parselet_with_string_no_quote_bounds(self):
    sp = StringParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.STRING, "abcdefg"))

  def test_string_parselet_with_string_value(self):
    sp = StringParselet()
    n = sp.parse(None, Token(TokenType.STRING, "\"hello\""))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, basestring)
    self.assertEqual(n.value, "hello")

  def test_set_parselet_with_non_set(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)): 
      sp.parse(None, Token(TokenType.SET, "(a, b, c)"))
      sp.parse(None, Token(TokenType.SET, "a, b, c"))
      sp.parse(None, Token(TokenType.SET, "[a, b, c"))
      sp.parse(None, Token(TokenType.SET, "a, b, c]"))
      sp.parse(None, Token(TokenType.SET, "<a, b, c>"))

  def test_set_parselet_with_nested_set(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a, b, [c,d]]"))

  def test_set_parselet_with_nested_map(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a, {b: c}, d]"))

  def test_set_parselet_with_non_comma_delimited(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a b c]"))
      sp.parse(None, Token(TokenType.SET, "[a | b | c]"))
      sp.parse(None, Token(TokenType.SET, "[a; b; c]"))

  def test_set_parselet_with_duplicates(self):
    sp = SetParselet()
    with(self.assertRaises(Exception)):
      sp.parse(None, Token(TokenType.SET, "[a, b, c, a]"))

  def test_set_parselet_with_valid_set(self):
    sp = SetParselet()
    n = sp.parse(None, Token(TokenType.SET, "[a, b, c]"))
    self.assertIsInstance(n, Node)
    self.assertIsInstance(n.value, list)
    self.assertEquals(len(n.value), 3)
    self.assertIn('a', n.value)
    self.assertIn('b', n.value)
    self.assertIn('c', n.value)

  def test_map_parselet_with_non_map(self):
    mp = MapParselet()
    with(self.assertRaises(Exception)):
      mp.parse(None, Token(TokenType.MAP, "(a, b, c)"))
      mp.parse(None, Token(TokenType.MAP, "a, b, c"))
      mp.parse(None, Token(TokenType.MAP, "{a, b, c"))
      mp.parse(None, Token(TokenType.MAP, "a, b, c}"))
      mp.parse(None, Token(TokenType.MAP, "<a, b, c>"))

