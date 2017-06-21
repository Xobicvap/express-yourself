
DEFAULT_DELIM=","
MAP_DELIM=":"
SET_BEGIN="["
SET_END="]"
MAP_BEGIN="{"
MAP_END="}"

def validate_numeric(st):
  if not st.isdigit():
    try :
      float(st)
    except ValueError:
      raise Exception("Value " + st + " parsed as numeric but is not")

def validate_string(st):
  if not isinstance(st, basestring):
    raise Exception("Value '" + str(st) + "' parsed as string but is not")
  if "\"" not in st:
    raise Exception("Value '" + st + "' not valid string; must be bounded by \"")

def split_strip(st, delim=','):
  return [x.strip() for x in st.split(delim)]

def remove_chars(st, removes):
  return filter(lambda x: x not in removes, st)

def remove_and_split(st, removes, delim):
  return split_strip(remove_chars(st, removes), delim)

def prevent_nested_type(st, begin, end, message):
  exmessage = message + "... offending token: " + st
  if len(filter(lambda x: x in begin, st)) > 1:
    raise Exception(exmessage)
  elif len(filter(lambda x: x in end, st)) > 1:
    raise Exception(exmessage)

def map_pairs_to_map(pairs, strmap={}):
  for p in pairs:
    if MAP_DELIM not in p:
      raise Exception("Maps must be formed with ':' as delimiter")
    head, tail = split_strip(p, MAP_DELIM)
    strmap[head] = tail
  return strmap

def map_parse(st):
  message = "Sorry, nested maps not supported yet"

  prevent_nested_type(st, [MAP_BEGIN], [MAP_END], message)
  pairs = remove_and_split(st, [MAP_BEGIN, MAP_END], DEFAULT_DELIM)
  return map_pairs_to_map(pairs)

def set_parse(st):
  message = "Sorry, nested sets not supported yet"
  validate_set(st)
  prevent_nested_type(st, [SET_BEGIN], [SET_END], message)
  strset = remove_and_split(st, [SET_BEGIN, SET_END], DEFAULT_DELIM)
  set_prevent_duplicates(strset)
  return strset

def validate_set(st):
  if SET_BEGIN not in st or SET_END not in st:
    raise Exception("Sets must be bounded by '" + SET_BEGIN + "' and '" + SET_END + "', " + st + " given")
  if st[0] != SET_BEGIN and st[-1] != SET_END:
    raise Exception("Sets must be bounded by '" + SET_BEGIN + "' and '" + SET_END + "', " + st + " given")
  if MAP_BEGIN in st or MAP_END in st:
    raise Exception("Sets may not contain maps, only scalars")
  if DEFAULT_DELIM not in st:
    raise Exception("Sets must be delimited by '" + DEFAULT_DELIM + "', " + st + " given")

def validate_map(st):
  if MAP_BEGIN not in st or MAP_END not in st:
    raise Exception("Maps must be bounded by '" + MAP_BEGIN + "' and '" + MAP_END + "', " + st + " given")
  if st[0] != MAP_BEGIN and st[-1] != MAP_END:
    raise Exception("Maps must be bounded by '" + MAP_BEGIN + "' and '" + MAP_END + "', " + st + " given")
  if SET_BEGIN in st or SET_END in st:
    raise Exception("Maps may not contain sets, only scalars")
  if DEFAULT_DELIM not in st:
    raise Exception("Maps must be delimited by '" + DEFAULT_DELIM + "', " + st + " given")

def set_prevent_duplicates(strset):
  if len(set(strset)) != len(strset):
    raise Exception("Duplicate elements found in set, this is not allowed")

