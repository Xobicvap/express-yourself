import re

class Tokenizer:
  """ Basically a wrapper class for re.scanner, the most ingenious piece of
      tokenizing code ever. 

      Attributes:
        tokendefs (list): list of 2-element tuples, in the following format:
          element 0: regular expression for token
          element 1: function of form lambda(scanner, token) which makes a
                     token (see example token defs)
        scanner (re.Scanner): scanner instance
  """
  def __init__(self, tokendefs):
    """ Registers the token definitions (see class docstring) and registers
        a scanner object using the token definitions.

        Arguments:
          tokendefs (list): see class docstring
    """
    self.tokendefs = tokendefs
    self.scanner = self.produce()

  def produce(self):
    """ Wrapper for scanner construction.
    """
    scanner = re.Scanner(self.tokendefs, flags=re.DOTALL)
    return scanner

  def tokenize(self, line):
    """ Wrapper for scanner.scan method. Returns the tokens produced.
        Arguments:
          line (str): line to scan
    """
    tokens, remainder = self.scanner.scan(line)
    return tokens

