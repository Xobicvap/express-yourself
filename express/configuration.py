
class Configuration:
  """ Class holding configuration definitions
      
      Attributes:
        operator_map (dict): map of operator symbols to operator types
        parselet_map (dict): map of token types to parselet types
        token_defs (dict): map of token definitions (using scanner)
  """

  def __init__(self):
    self.operator_map = None
    self.parselet_map = None
    self.token_defs = None

  def set_config(self, configtype, configmap):
    """ Sets config type specified.
        Arguments:
          configtype (str): name of config to set (operator/parselet/token)
          configmap (dict): config map to set for this type
    """
    if configtype == "operator":
      self.operator_map = configmap
    elif configtype == "parselet":
      self.parselet_map = configmap
    elif configtype == "token":
      self.token_defs = configmap
    else:
      raise Exception(configtype + " is not understood as a configuration option")

  def get_token_defs(self):
    """ Gets token definitions that have been set.
    """
    return self.token_defs

  def get_operator_map(self):
    """ Gets the operator map for this configuration.
    """
    return self.operator_map

  def get_parselet_map(self):
    """ Gets the parselet map for this configuration.
    """
    return self.parselet_map
