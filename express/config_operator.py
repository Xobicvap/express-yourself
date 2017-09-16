from operators import *

operator_map = {
  "=" : AssignOperator(),
  "+" : AddOperator(),
  "-" : SubtractOperator(),
  "*" : MultiplyOperator(),
  "/" : DivisionOperator(),
  "?..": RandrangeOperator()
}
