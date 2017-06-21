from base_operator import Operator
from random import choice, randrange

class AssignOperator(Operator):
  """ Operator used for assignment of a value to a variable.
      The value can be a variable in and of itself, or an
      expression, or a simple value.
  """
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
