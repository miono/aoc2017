#!/usr/bin/env python

import operator
record = 0
instructions = []
registers = {
        'acc' : 0,
        'ar' : 0,
        'bb' : 0,
        'bq' : 0,
        'cli' : 0,
        'ec' : 0,
        'ej' : 0,
        'fe' : 0,
        'foz' : 0,
        'h' : 0,
        'hb' : 0,
        'ln' : 0,
        'nev' : 0,
        'nfo' : 0,
        'piw' : 0,
        'qym' : 0,
        're' : 0,
        's' : 0,
        'tem' : 0,
        'tl' : 0,
        'u' : 0,
        'xuu' : 0,
        'yxr' : 0
}
ops = {'==' : operator.eq,
       '!=' : operator.ne,
       '<=' : operator.le,
       '>=' : operator.ge,
       '>'  : operator.gt,
       '<'  : operator.lt}

f = open('input').readlines()

for i, line in enumerate(f):
  line = line.rstrip().split()
  instructions.append([line[0], line[1], int(line[2]), line[3], line[4], line[5], int(line[6])])

for instruction in instructions:
  if ops[instruction[5]](registers[instruction[4]], instruction[6]):
    if instruction[1] == 'inc':
      new_val = registers[instruction[0]] + instruction[2]
      if new_val > record:
        record = new_val
      registers[instruction[0]] = new_val
    if instruction[1] == 'dec':
      new_val = registers[instruction[0]] - instruction[2]
      if new_val > record:
        record = new_val
      registers[instruction[0]] = new_val


print record
