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
  """ Operator for simple addition.
  """
  def __init__(self):
    self.fn = lambda x,y: x + y

class SubtractOperator(Operator):
  """ Operator for subtraction.
  """
  def __init__(self):
    self.fn = lambda x,y: x - y

class MultiplyOperator(Operator):
  """ Operator for multiplication.
  """
  def __init__(self):
    self.fn = lambda x,y: x * y

class DivisionOperator(Operator):
  """ Operator for division
  """
  def __init__(self):
    self.fn = lambda x,y: x / y

class RandrangeOperator(Operator):
  """ Operator to choose a value randomly from the range
      specified by x and y (lower and upper bounds, respectively).
  """
  def __init__(self):
    self.fn = lambda x,y: randrange(x, y+1)

class RandchoiceOperator(Operator):
  """ Operator to randomly choose a value from the supplied collection (x).
  """
  def __init__(self):
    self.fn = lambda x: choice(x)
