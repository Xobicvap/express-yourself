from random import randrange, choice

class Operator:
  def process(self, envir, result, name=None):
    envir.varRepo().setVar(str(name), result)

  def evaluate(self, left, right, envir):
    lval = left.evaluate(envir)
    if right is not None:
      rval = right.evaluate(envir)
      result = self.fn(lval, rval)
    else:
      result = self.fn(lval)
    self.process(envir, result, "_last")
    return result

class AssignOperator(Operator):
  def evaluate(self, left, right, envir):
    self.process(envir, right.evaluate(envir), left.value)
    return None

class AddOperator(Operator):
  def __init__(self):
    self.fn = lambda x,y: x + y

class SubtractOperator(Operator):
  def __init__(self):
    self.fn = lambda x,y: x - y

class MultiplyOperator(Operator):
  def __init__(self):
    self.fn = lambda x,y: x * y

class DivisionOperator(Operator):
  def __init__(self):
    self.fn = lambda x,y: x / y

class RandrangeOperator(Operator):
  def __init__(self):
    self.fn = lambda x,y: randrange(x, y+1)

class RandchoiceOperator(Operator):
  def __init__(self):
    self.fn = lambda x: choice(x)
