import imp
from var_repo import VarRepo
from configurator import Configurator
from tokenizer import Tokenizer

class Environment:

  def __init__(self, config_location):
    if not config_location.strip():
      raise Exception("Provide location of config file")
    self.config_location = config_location
    self.var_repo = VarRepo()
  
  def load_config_module(self):
    m = imp.load_source("config", self.config_location)
    return m

  def config(self):
    m = self.load_config_module()
    configure = Configurator(m.operator_map, m.parselet_map)
    self.parser_instance = configure.makeParser()
    print(m.token_defs)
    self.tokenizer = Tokenizer(m.token_defs)
    self.configurator = configure
    
    return self

  def parser(self, line):
    if self.parser_instance is None:
      self.config()
    tokens = self.tokenizer.tokenize(line)
    self.parser_instance.token_define(tokens)
    return self.parser_instance

  def operator(self, operator_str):
    return self.configurator.makeOperator(operator_str)

  def varRepo(self):
    return self.var_repo
