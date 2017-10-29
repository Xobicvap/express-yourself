import imp
from var_repo import VarRepo
from configurator import Configurator
from tokenizer import Tokenizer
from config_loader import ConfigLoader

class Environment:
  """ Class responsible for holding the state of the parser and its various
      tools.

      Attributes:
        configurator (Configurator): used to generate parser and other tools
        var_repo (dict): variable store
        parser_instance (Parser): built via configurator
        tokenizer (Tokenizer): built via configurator
  """
  def __init__(self, config_kwargs = None):
    """ Given the configuration options specified, build the parser
        environment.

        Arguments:
          config_kwargs (dict): options for configuration, see config_loader
    """
    if not config_kwargs:
      config_kwargs = {}
    self.configurator = Configurator(ConfigLoader(**config_kwargs).load())
    self.var_repo = VarRepo()
    self.parser_instance = None
    self.tokenizer = None
  
  def config(self):
    """ Uses configurator to build the parser and tokenizer.
    """
    self.parser_instance = self.configurator.make_parser()
    self.tokenizer = self.configurator.make_tokenizer()
    return self

  def parser(self, line):
    """ Parses the supplied line using the parser and tokenizer.
        Arguments:
          line (str): line of text to parse
    """
    if self.parser_instance is None:
      self.config()
    tokens = self.tokenizer.tokenize(line)
    self.parser_instance.token_define(tokens)
    return self.parser_instance

  def operator(self, operator_str):
    """ Creates an operator from the operator string supplied
        Arguments:
          operator_str (str): symbol etc corresponding to operator
    """
    return self.configurator.make_operator(operator_str)

  def get_var_repo(self):
    """ Returns the current variable repo.
    """
    return self.var_repo
