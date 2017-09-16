import os
import imp
from configuration import Configuration

class ConfigLoader:
  """
  Handles the various ways token/parselet/operator definitions are parsed 
  and loaded.

  Default behavior (no options specified):
    Loads default operator/token/parselet definitions.

  Options permitted:
    config_location
      Specify the full path to your configuration files (must be Python syntax)
    X_use_default, where X is operator/parselet/token
      Defaults to True; tells Express Yourself to use the default definitions.
    X_merge_default, where X is operator/parselet/token
      Defaults to False unless X_use_default is True as well;
      instructs Express Yourself to merge your definitions with the defaults.
      
      Any definitions you override specifically will be overridden; any you do 
      not specify will use the default.

    If you only specify config_location in the above dict, only your 
    definitions will be used.

  Here are some examples of how to set options for this class. If there is

  Examples:
  config = {
    "config_location": "/path/to/your/definitions"
  }
  This will use only your operator / parselet / token definitions. Do not 
  expect to use any you are not explicitly defining.

  config = {}
  This will use only the out-of-the-box Express Yourself definitions.

  config = {
    "config_location": "/path/to/your/definitions",
    "operator_use_default": True,
    "operator_merge_default": True,
    "parselet_use_default": True,
    "parselet_merge_default": True,
    "token_use_default": True,
    "token_merge_default": True
  }
  This will load the default definitions and merge in yours. The ideal use case
  here is if you have some custom definitions you want to use but you also
  want to use the built-in definitions. Using options in this way will give
  you both.

  config = {
    "config_location": "/path/to/your/definitions",
    "operator_use_default": True,
    "operator_merge_default": False,
    "token_use_default": False
  }
  This will use default definitions for operators and parselets, but let
  you define your own tokens. Note that the parselet section is removed as
  the default behavior is to just use the default definitions without merging.
  
  Note that operator_merge_default set explicitly False here is redundant;
  you can do so for readability but unless it is set True there will be
  no merging.

  """
  def __init__(self, **kwargs):
    """ Creates a ConfigLoader instance. See the class definition for how to
        specify the kwargs dictionary expected.

        Attributes:
          config_location (str): Full path to your configuration files. Optional.
          operator_use_default (boolean): Use default operator defs. Defaults True.
          parselet_use_default (boolean): Use default parselet defs. Defaults True.
          token_use_default (boolean): Use default token defs. Defaults True.
          operator_merge_default (boolean): Merge default defs with user defs.
            Defaults False unless set explicitly and use_default set True.
          parselet_merge_default (boolean): Merge default defs with user defs.
            Defaults False unless set explicitly and use_default set True.
          token_merge_default (boolean): Merge default defs with user defs.
            Defaults False unless set explicitly and use_default set True.
          config_types (list): List of types to manage
          config_map (dict): mapping of types to module attribute names
    """
    op_merge = kwargs.get("operator_merge_default")
    pa_merge = kwargs.get("parselet_merge_default")
    to_merge = kwargs.get("token_merge_default")
    config_location = kwargs.get("config_location")
    if op_merge or pa_merge or to_merge:
      if config_location is None:
        raise Exception("You have specified merging user configs with defaults but no user configs specified...")
    op_default = kwargs.get("operator_use_default", True)
    pa_default = kwargs.get("parselet_use_default", True)
    to_default = kwargs.get("token_use_default", True)
    self.operator_use_default = op_default
    self.parselet_use_default = pa_default
    self.token_use_default = to_default

    self.operator_merge_default = True if op_merge and op_default else False
    self.parselet_merge_default = True if pa_merge and pa_default else False
    self.token_merge_default = True if to_merge and to_default else False
    self.config_location = config_location
    self.config_types = ["operator", "parselet", "token"]
    self.config_map = {
      "operator": "operator_map",
      "parselet": "parselet_map",
      "token": "token_defs"
    }
    self.get_default_config_location()

  def load(self):
    """
    Creates a Configuration object for use by the Express Yourself environment.
    Loads in operator, parselet, and token definitions as per options set at
    instantiation. See class definition for details.
    """
    conf = Configuration()
    for configtype in self.config_types:
      if configtype == "operator":
        use_default = self.operator_use_default
        merge_default = self.operator_merge_default
      elif configtype == "parselet":
        use_default = self.parselet_use_default
        merge_default = self.parselet_merge_default
      elif configtype == "token":
        use_default = self.token_use_default
        merge_default = self.token_merge_default
      conf.set_config(configtype, self.load_config_type(configtype, use_default, merge_default))
    return conf

  def get_default_config_location(self):
    """
    Gets the default config path, AKA wherever this module lives.
    """
    thisdir = os.path.dirname(os.path.realpath(__file__))
    self.default_config_location = thisdir

  def load_config_type(self, configtype, use_default, merge_default):
    """
    Loads the module associated with this config type and returns the desired 
    definitions.

    Performs merging if specified by merge_default.

    Arguments:
      configtype (str): The type of config to load (operator, parselet, token)
      use_default (boolean): Whether or not to load default config definitions.
      merge_default (boolean): If true, merges default defs with user defs.
    """
    if use_default:
      default_conf = self.load_config(configtype, self.default_config_location)
      if merge_default:
        config = self.load_config(configtype, self.config_location) 
        return self.merge_configs(default_conf, config)
      else:
        return default_conf
    else:
      config = self.load_config(configtype, self.config_location) 
      return config
  
  def merge_configs(self, config1, config2):
    """ Merges two definition maps.

        Arguments:
          config1 (dict): Configuration dictionary to override
          config2 (dict): Configuration dictionary that overlays on top of config1
    """
    mapcopy = config1.copy()
    mapcopy.update(config2)
    return mapcopy

  def load_config(self, configtype, location):
    """ Loads the appropriate map from the configuration module specified.

        Arguments:
          configtype (str): The type of config to load (operator, parselet, token)
          location (str): The full path to the config module to load
    """
    m = self.load_config_module(configtype, location)
    return self.get_config_type(configtype, m)

  def load_config_module(self, configtype, location):
    """ Given the config type and path (location), loads the module specified

        Arguments:
          configtype (str): The type of config to load (operator, parselet, token)
          location (str): The full path to the config module to load
    """
    configname = "config_" + configtype
    config_filename = configname + ".py"
    configfile = os.path.join(location, config_filename)
    m = imp.load_source(configname, configfile)
    return m

  def get_config_type(self, configtype, m):
    """ Given a configuration module, get the appropriate definition map from it

        Arguments:
          configtype (str): The type of config to load (operator, parselet, token)
          m (module): The configuration module to obtain the desired map from
    """
    if configtype not in self.config_map:
      raise Exception("Unrecognized config type " + configtype)
    config_attr = self.config_map[configtype]
    return getattr(m, config_attr)

