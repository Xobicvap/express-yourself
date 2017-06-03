class VarRepo:
  def __init__(self):
    self.repo = {}

  def setVar(self, name, value):
    self.repo[name] = value
