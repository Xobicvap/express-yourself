from configurator import Configurator
from parser import Parser
import unittest

class ConfiguratorTest(unittest.TestCase):

  def testMakeParser(self):
    configure = Configurator({"a": "b"}, {"a": "b"})
    parser = configure.makeParser()
    self.assertTrue(isinstance(parser, Parser))
