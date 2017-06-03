import re

class Tokenizer:

  def __init__(self, tokendefs):
    self.tokendefs = tokendefs
    self.scanner = self.produce()

  def produce(self):
    scanner = re.Scanner(self.tokendefs, flags=re.DOTALL)
    return scanner

  def tokenize(self, line):
    tokens, remainder = self.scanner.scan(line)
    return tokens

