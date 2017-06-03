from operator_map import operator_map, get_operator

class Node:
  def __init__(self, value, left=None, right=None):
    self.left=left
    self.right=right
    self.value=value

  def getValue(self, var_repo):
    if hasattr(self.value, 'value'):
      return var_repo.repo[self.value.value]
    return self.value

  def evaluate(self, var_repo):
    if self.left is not None or self.right is not None:
      oper = get_operator(self.value)
      return oper.evaluate(self.left, self.right, var_repo)
    else:
      return self.getValue(var_repo)

def print_tree(tree, level=0):
  if tree is None:
    return
  if tree.right is not None:
    print_tree(tree.right, level+1)
  print("\t"*level + str(tree.value))
  if tree.left is not None:
    print_tree(tree.left, level+1)
