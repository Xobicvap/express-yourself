class VarRepo:
  def __init__(self):
    self.repo = {}

  def set_var(self, name, value):
    self.repo[name] = value
