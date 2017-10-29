from random import randrange, choice

""" The Operator module contains classes used to perform operations
    Some basic operations are included in Express Yourself, but
    if you need more (and you probably will), you can extend the
    base Operator class.
"""

class Operator:
  """ Base class for operators. Will not do anything on its own since
      its internal function is not defined.
      
      Operators do two basic things: evaluate a node to produce a result,
      and store said result in a variable repository. The methods
      to do that are evaluate and process, respectively.

      Each operator subclass is defined with an internal function it
      uses to do its job. This can be anything callable.
  """
  def process(self, envir, result, name=None):
    """ Uses the environment param (envir) to store the result of 
        an operation in the environment variable repository.

        Arguments:
          envir (Environment): environment instance
          result (any): Result of previous operation to be stored in
            environment's variable repository
          name (:obj: `str`, optional): Name of variable to set, if applicable.
    """
    envir.get_var_repo().set_var(str(name), result)

  def evaluate(self, left, right, envir):
    """ Evaluates a node.

        The left node is evaluated first, then, if the right node is
        present, it is evaluated then both values are passed to the
        internal evaluator function.

        If there is no right node, the left value is passed to the
        internal function.

        The result of the operation is returned.
    """
    lval = left.evaluate(envir)
    if right is not None:
      rval = right.evaluate(envir)
      result = self.fn(lval, rval)
    else:
      result = self.fn(lval)
    self.process(envir, result, "_last")
    return result
