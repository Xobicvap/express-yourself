import unittest
from config_loader import ConfigLoader

class ConfigLoaderTest(unittest.TestCase):

  def test_init_no_user_configs_but_merge_specified(self):
    kwargs = {"operator_merge_default": "eh"}
    with(self.assertRaises(Exception)):
      cl = ConfigLoader(**kwargs)
    kwargs = {"token_merge_default": "eh"}
    with(self.assertRaises(Exception)):
      cl = ConfigLoader(**kwargs)
    kwargs = {"parselet_merge_default": "eh"}
    with(self.assertRaises(Exception)):
      cl = ConfigLoader(**kwargs)

  def test_init_no_merge_if_both_not_true(self):
    kwargs = {
      "operator_merge_default": True,
      "config_location": "eh",
      "operator_use_default": False
    }
    cl = ConfigLoader(**kwargs)
    self.assertFalse(cl.operator_merge_default)

    kwargs = {
      "parselet_merge_default": True,
      "config_location": "eh",
      "parselet_use_default": False
    }
    cl = ConfigLoader(**kwargs)
    self.assertFalse(cl.parselet_merge_default)

    kwargs = {
      "token_merge_default": True,
      "config_location": "eh",
      "token_use_default": False
    }
    cl = ConfigLoader(**kwargs)
    self.assertFalse(cl.token_merge_default)

  def test_init_merge_defaults_when_use_default_not_present(self):
    kwargs = {
      "operator_merge_default": True,
      "config_location": "eh"
    }
    cl = ConfigLoader(**kwargs)
    self.assertTrue(cl.operator_merge_default)

    kwargs = {
      "parselet_merge_default": True,
      "config_location": "eh"
    }
    cl = ConfigLoader(**kwargs)
    self.assertTrue(cl.parselet_merge_default)

    kwargs = {
      "token_merge_default": True,
      "config_location": "eh"
    }
    cl = ConfigLoader(**kwargs)
    self.assertTrue(cl.token_merge_default)

  def test_init_merge_defaults_when_use_default_present(self):
    kwargs = {
      "operator_merge_default": True,
      "config_location": "eh",
      "operator_use_default": True 
    }
    cl = ConfigLoader(**kwargs)
    self.assertTrue(cl.operator_merge_default)

    kwargs = {
      "parselet_merge_default": True,
      "config_location": "eh",
      "parselet_use_default": True
    }
    cl = ConfigLoader(**kwargs)
    self.assertTrue(cl.parselet_merge_default)

    kwargs = {
      "token_merge_default": True,
      "config_location": "eh",
      "token_use_default": True
    }
    cl = ConfigLoader(**kwargs)
    self.assertTrue(cl.token_merge_default)

  def test_init_use_defaults_by_default(self):
    kwargs = {}
    cl = ConfigLoader(**kwargs)
    self.assertTrue(cl.operator_use_default)
    self.assertTrue(cl.parselet_use_default)
    self.assertTrue(cl.token_use_default)

  # @TODO: make tests for other things after we can mock
  # or otherwise account for module loading / pathing

