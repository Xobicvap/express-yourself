class Node:
  """ Class representing a node in an expression tree.

      Attributes:
        value (any): value of this node
        left (any, optional): left child
        right (any, optional): right child
  """
  def __init__(self, value, left=None, right=None):
    """ Sets left child, right child (if either are present), and value
    """
    self.left=left
    self.right=right
    self.value=value

  def get_value(self, envir):
    """ Gets the value of this node. 
        If the value is set as a Variable, look up the current value in the
        variable repository of the environment passed in.
        Otherwise returns the value as-is.

        Arguments:
          envir (Environment): Environment instance
    """
    if hasattr(self.value, 'value'):
      return envir.get_var_repo().repo[self.value.value]
    return self.value

  def evaluate(self, envir):
    """ Evaluates this node, assuming this node is an operator
        Arguments:
          envir (Environment): container for parser and tools etc
    """
    if self.left is not None or self.right is not None:
      return envir.operator(self.value).evaluate(self.left, self.right, envir)
    else:
      return self.get_value(envir)

def print_tree(tree, level=0):
  if tree is None:
    return
  if tree.right is not None:
    print_tree(tree.right, level+1)
  print("\t"*level + str(tree.value))
  if tree.left is not None:
    print_tree(tree.left, level+1)
