from node import Node
from var_repo import VarRepo
from variable import Variable
import unittest

class TestEnvir:
  def __init__(self, var_repo = None):
    if var_repo is not None:
      self.var_repo = var_repo
  def varRepo(self):
    return self.var_repo or VarRepo()

class NodeTest(unittest.TestCase):

  def testGetValueGetsSimpleValue(self):
    n1 = Node("1")
    te = TestEnvir()
    v = n1.getValue(te)
    self.assertEqual('1', v)

  def testGetValueGetsVariableValue(self):
    n1 = Node(Variable("Abcdefg"))
    vr = VarRepo()
    vr.setVar("Abcdefg", 1)
    te = TestEnvir(vr)
    v = n1.getValue(te)
    self.assertEqual(1, v)
  
  def testEvaluateNonOperatorNodeAsVariable(self):
    n1 = Node(Variable("Abcdefg"))
    vr = VarRepo()
    vr.setVar("Abcdefg", 1)
    te = TestEnvir(vr)
    v = n1.evaluate(te)
    self.assertEqual(1, v)
