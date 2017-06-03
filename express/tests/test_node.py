from node import Node
from var_repo import VarRepo
from variable import Variable
import unittest

class NodeTest(unittest.TestCase):

  def testGetValueGetsSimpleValue(self):
    n1 = Node("1")
    vr = VarRepo()
    v = n1.getValue(vr)
    self.assertEqual('1', v)

  def testGetValueGetsVariableValue(self):
    n1 = Node(Variable("Abcdefg"))
    vr = VarRepo()
    vr.setVar("Abcdefg", 1)
    v = n1.getValue(vr)
    self.assertEqual(1, v)

  def testEvaluateNonOperatorNodeAsVariable(self):
    n1 = Node(Variable("Abcdefg"))
    vr = VarRepo()
    vr.setVar("Abcdefg", 1)
    v = n1.evaluate(vr)
    self.assertEqual(1, v)

  def testEvaluateNonOperatorNodeAsVariable(self):
    n1 = Node("abcd")
    n2 = Node(5.0)
    vr = VarRepo()
    v1 = n1.evaluate(vr)
    v2 = n2.evaluate(vr)
    self.assertEqual("abcd", v1)
    self.assertEqual(5.0, v2)

