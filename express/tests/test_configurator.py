from configurator import Configurator
from parser import Parser
from tokenizer import Tokenizer
from configuration import Configuration
from parselets import PrefixParselet, InfixParselet
import unittest

class ConfiguratorTest(unittest.TestCase):

  def test_make_parser(self):
    parselet_map = {
      0: PrefixParselet,
      1: InfixParselet,
      2: InfixParselet
    }
    configuration = Configuration()
    configuration.set_config("parselet", parselet_map)
        
    configurator = Configurator(configuration)
    parser = configurator.make_parser()
    self.assertEquals(1, len(parser.prefix_parselets))
    self.assertEquals(2, len(parser.infix_parselets))

  def test_make_parser_with_weird_parselet_type(self):
    parselet_map = {
      0: PrefixParselet,
      1: basestring
    }
    configuration = Configuration()
    configuration.set_config("parselet", parselet_map)
        
    configurator = Configurator(configuration)
    with(self.assertRaises(Exception)):
      parser = configurator.make_parser()

  def test_make_tokenizer(self):
    tokendefs = [
      (r"[A-Z]", None)
    ]
    configuration = Configuration()
    configuration.set_config("token", tokendefs)

    configurator = Configurator(configuration)
    tokenizer = configurator.make_tokenizer()
    self.assertTrue(isinstance(tokenizer, Tokenizer) )

  def test_make_operator(self):
    operatordefs = {
      "=": "thingie"
    }
    configuration = Configuration()
    configuration.set_config("operator", operatordefs)

    configurator = Configurator(configuration)
    operator = configurator.make_operator("=")
    self.assertEquals("thingie", operator)

  def test_make_operator_with_unknown_value(self):
    operatordefs = {
      "=": "thingie"
    }
    configuration = Configuration()
    configuration.set_config("operator", operatordefs)

    configurator = Configurator(configuration)
    with(self.assertRaises(Exception)):
      operator = configurator.make_operator("&")
