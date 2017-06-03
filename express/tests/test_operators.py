from operators import *
from var_repo import VarRepo
import unittest

class MockNode:

  def __init__(self, value):
    self.value = value

  def evaluate(self):
    return self.value


class OperatorTest(unittest.TestCase):

  def testAssignOperatorEvaluate(self):
    n1 = MockNode("A")
    n2 = MockNode(1)

    ao = AssignOperator()
    vr = VarRepo()
    ao.evaluate(n1, n2, vr)

    self.assertEqual({"A": 1}, vr.repo)

  def testAddOperatorEvaluate(self):
    n1 = MockNode(1)
    
    ao = AddOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n1, vr)

    self.assertEqual(2, result)
    self.assertEqual({"_last": 2}, vr.repo)

  def testSubtractOperatorEvaluate(self):
    n1 = MockNode(1)
    
    ao = SubtractOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n1, vr)

    self.assertEqual(0, result)
    self.assertEqual({"_last": 0}, vr.repo)

  def testMultiplyOperatorEvaluate(self):
    n1 = MockNode(2)
    n2 = MockNode(2)
    
    ao = MultiplyOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n2, vr)

    self.assertEqual(4, result)
    self.assertEqual({"_last": 4}, vr.repo)

  def testDivisionOperatorEvaluate(self):
    n1 = MockNode(4)
    n2 = MockNode(2)
    
    ao = DivisionOperator()
    vr = VarRepo()
    result = ao.evaluate(n1, n2, vr)

    self.assertEqual(2, result)
    self.assertEqual({"_last": 2}, vr.repo)


if __name__ == "__main__":
  unittest.main()
