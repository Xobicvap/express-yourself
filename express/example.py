from environment import Environment
from node import print_tree

env = Environment()
l1 = "A = 5"
l2 = "B = A + 5"
l3 = "C = B * 5"
l4 = "D = C / B"
l5 = "E = C * 2"
l6 = "F = 1 ?.. E"

def parsing_please(line, env):
  print "Parsing: " + line
  node = env.parser(line).parse_expression()
  print_tree(node)
  node.evaluate(env)
  print env.get_var_repo().repo
  print "\n"

lines = [l1, l2, l3, l4, l5, l6]

for line in lines:
  parsing_please(line, env)


