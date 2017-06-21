
class Node:
  def __init__(self, value, left=None, right=None):
    self.left=left
    self.right=right
    self.value=value

  def getValue(self, envir):
    if hasattr(self.value, 'value'):
      return envir.varRepo().repo[self.value.value]
    return self.value

  def evaluate(self, envir):
    if self.left is not None or self.right is not None:
      return envir.operator(self.value).evaluate(self.left, self.right, envir)
    else:
      return self.getValue(envir)

def print_tree(tree, level=0):
  if tree is None:
    return
  if tree.right is not None:
    print_tree(tree.right, level+1)
  print("\t"*level + str(tree.value))
  if tree.left is not None:
    print_tree(tree.left, level+1)
