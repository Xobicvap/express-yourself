from parser import Parser
from tokenizer import Tokenizer

class Configurator:
  """ Class responsible for creating objects needed by environment.
      
      Attributes:
        config (Configuration): Configuration instance
  """
  def __init__(self, configuration):
    """ Instantiate with a Configuration instance.
        Arguments:
          configuration (Configuration): contains operator/parselet/token defs
    """
    self.config = configuration

  def make_parser(self):
    """ Creates a Parser instance.

        Override this method to create a Parser of your own.
    """
    parser = Parser()
    parselet_map = self.config.get_parselet_map()
    for tokentype, parselet in parselet_map:
      parser.register(tokentype, parselet)

    return parser

  def make_tokenizer(self):
    """ Creates a Tokenizer instance.

        Override this method to create your own Tokenizer.
    """
    tokenizer = Tokenizer(self.config.get_token_defs())
    return tokenizer

  def make_operator(self, value):
    """ Creates an Operator based on the given value.

        Attributes:
           value (str): string token used for operator
    """
    if value not in self.config.get_operator_map():
      raise Exception(value + " not recognized as operator")
    return self.config.get_operator_map()[value]

