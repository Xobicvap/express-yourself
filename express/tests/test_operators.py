from operators import *
from var_repo import VarRepo
from node import Node
import unittest

class OperatorTest(unittest.TestCase):

  def testAssignOperatorEvaluate(self):
    n1 = Node("A")
    n2 = Node(1)

    ao = AssignOperator()
    vr = VarRepo()
    ao.evaluate(n1, n2, vr)

    self.assertEqual({"A": 1}, vr.repo)

  def testAddOperatorEvaluate(self):
    n1 = Node(1)
    
    ao = AddOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n1, vr)

    self.assertEqual(2, result)
    self.assertEqual({"_last": 2}, vr.repo)

  def testSubtractOperatorEvaluate(self):
    n1 = Node(1)
    
    ao = SubtractOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n1, vr)

    self.assertEqual(0, result)
    self.assertEqual({"_last": 0}, vr.repo)

  def testMultiplyOperatorEvaluate(self):
    n1 = Node(2)
    n2 = Node(2)
    
    ao = MultiplyOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n2, vr)

    self.assertEqual(4, result)
    self.assertEqual({"_last": 4}, vr.repo)

  def testDivisionOperatorEvaluate(self):
    n1 = Node(4)
    n2 = Node(2)
    
    ao = DivisionOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n2, vr)

    self.assertEqual(2, result)
    self.assertEqual({"_last": 2}, vr.repo)

