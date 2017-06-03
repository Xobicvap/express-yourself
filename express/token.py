
class Token:
  def __init__(self, tokentype, value):
    self.tokentype = tokentype
    self.value = value

  def getType(self):
    return self.tokentype

  def getValue(self):
    return self.value

  def __str__(self):
    return self.value

