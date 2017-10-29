from node import Node
from var_repo import VarRepo
from variable import Variable
import unittest

class TestEnvir:
  def __init__(self, var_repo = None):
    if var_repo is not None:
      self.var_repo = var_repo
  def get_var_repo(self):
    return self.var_repo or VarRepo()

class NodeTest(unittest.TestCase):

  def test_get_value_gets_simple_value(self):
    n1 = Node("1")
    te = TestEnvir()
    v = n1.get_value(te)
    self.assertEqual('1', v)

  def test_get_value_gets_variable_value(self):
    n1 = Node(Variable("Abcdefg"))
    vr = VarRepo()
    vr.set_var("Abcdefg", 1)
    te = TestEnvir(vr)
    v = n1.get_value(te)
    self.assertEqual(1, v)
  
  def test_evaluate_non_operator_node_as_variable(self):
    n1 = Node(Variable("Abcdefg"))
    vr = VarRepo()
    vr.set_var("Abcdefg", 1)
    te = TestEnvir(vr)
    v = n1.evaluate(te)
    self.assertEqual(1, v)
