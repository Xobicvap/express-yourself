from random import randrange

class Operator:
  def process(self, var_repo, result, name=None):
    var_repo.setVar(str(name), result)

  def evaluate(self, left, right, var_repo):
    lval = left.evaluate(var_repo)
    rval = right.evaluate(var_repo)
    result = self.fn(lval, rval)
    self.process(var_repo, result, "_last")
    return result

class AssignOperator(Operator):
  def evaluate(self, left, right, var_repo):
    self.process(var_repo, right.evaluate(var_repo), left.value)
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


