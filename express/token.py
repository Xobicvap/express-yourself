
class Token:
  def __init__(self, tokentype, value):
    self.tokentype = tokentype
    self.value = value

  def get_type(self):
    return self.tokentype

  def get_value(self):
    return self.value

  def __str__(self):
    return self.value

