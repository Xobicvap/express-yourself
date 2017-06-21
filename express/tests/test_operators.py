from operators import *
from var_repo import VarRepo
from node import Node
import unittest

class TestEnv:
  def __init__(self, var_repo = None):
    self.var_repo = var_repo or VarRepo()

  def varRepo(self):
    return self.var_repo
    

class OperatorTest(unittest.TestCase):

  def testAssignOperatorEvaluate(self):
    n1 = Node("A")
    n2 = Node(1)

    ao = AssignOperator()
    te = TestEnv()
    ao.evaluate(n1, n2, te)
    vr = te.varRepo()
    self.assertEqual({"A": 1}, vr.repo)

  def testAddOperatorEvaluate(self):
    n1 = Node(1)
    n2 = Node(1)
    
    ao = AddOperator()
    te = TestEnv()
    result = ao.evaluate(n1, n2, te)
    vr = te.varRepo()

    self.assertEqual(2, result)
    self.assertEqual({"_last": 2}, vr.repo)

  def testSubtractOperatorEvaluate(self):
    n1 = Node(1)
    
    ao = SubtractOperator()
    te = TestEnv()
    result = ao.evaluate(n1, n1, te)
    vr = te.varRepo()

    self.assertEqual(0, result)
    self.assertEqual({"_last": 0}, vr.repo)

  def testMultiplyOperatorEvaluate(self):
    n1 = Node(2)
    n2 = Node(2)
    
    ao = MultiplyOperator()
    te = TestEnv()
    result = ao.evaluate(n1, n2, te)
    vr = te.varRepo()

    self.assertEqual(4, result)
    self.assertEqual({"_last": 4}, vr.repo)

  def testDivisionOperatorEvaluate(self):
    n1 = Node(4)
    n2 = Node(2)
    
    ao = DivisionOperator()
    te = TestEnv()
    result = ao.evaluate(n1, n2, te)
    vr = te.varRepo()

    self.assertEqual(2, result)
    self.assertEqual({"_last": 2}, vr.repo)

  def testRandrangeOperatorEvaluate(self):
    n1 = Node(1)
    n2 = Node(3)
    rro = RandrangeOperator()
    te = TestEnv()
    result = rro.evaluate(n1, n2, te)
    
    self.assertIn(result, [1,2,3])

  def testRandchoiceOperatorEvaluate(self):
    n1 = Node([1,2,3])
    rco = RandchoiceOperator()
    te = TestEnv()
    result = rco.evaluate(n1, None, te)

    self.assertIn(result, [1,2,3])
