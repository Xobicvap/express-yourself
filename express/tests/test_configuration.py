from configuration import Configuration
import unittest

class ConfigurationTest(unittest.TestCase):

  def test_set_config_set_bad_config_type(self):
    config = Configuration()
    badtypes = ["", None, "?", "foperator", 3]
    for badtype in badtypes:
      with(self.assertRaises(Exception)):
        config.set_config(badtype, {})

  def test_set_config_set_operators(self):
    config = Configuration()
    configmap = {"a": "b"}
    config.set_config("operator", configmap)
    self.assertEquals(configmap, config.get_operator_map())
    self.assertEquals(None, config.get_parselet_map())
    self.assertEquals(None, config.get_token_defs())

  def test_set_config_set_parselets(self):
    config = Configuration()
    configmap = {"a": "b"}
    config.set_config("parselet", configmap)
    self.assertEquals(None, config.get_operator_map())
    self.assertEquals(configmap, config.get_parselet_map())
    self.assertEquals(None, config.get_token_defs())

  def test_set_config_set_tokens(self):
    config = Configuration()
    configmap = {"a": "b"}
    config.set_config("token", configmap)
    self.assertEquals(None, config.get_operator_map())
    self.assertEquals(None, config.get_parselet_map())
    self.assertEquals(configmap, config.get_token_defs())
