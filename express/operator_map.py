from operators import *

operator_map = {
  "=" : AssignOperator(),
  "+" : AddOperator(),
  "-" : SubtractOperator(),
  "*" : MultiplyOperator(),
  "/" : DivisionOperator(),
  "?..": RandrangeOperator()
}

def get_operator(text):
  return operator_map[text]
