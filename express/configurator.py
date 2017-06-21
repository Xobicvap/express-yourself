from parser import Parser

class Configurator:
  def __init__(self, operator_map, parselet_map):
    self.operator_map = operator_map
    self.parselet_map = parselet_map

  def makeParser(self):
    parser = Parser()
    for tokentype, parselet in self.parselet_map.items():
      parser.register(tokentype, parselet)
    return parser

  def makeOperator(self, value):
    if value not in self.operator_map:
      raise Exception(value + " not recognized as operator")
    return self.operator_map[value]

