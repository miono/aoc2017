#!/usr/bin/env python

import operator
import sys

for line in sys.stdin:
  inp = line.strip()
lengths = []
hashlist = [i for i in xrange(256)]
curpos = 0
skipsize = 0
suffixes = [17, 31, 73, 47, 23]

for char in inp:
  lengths.append(ord(char))

for number in suffixes:
  lengths.append(number)

def twist_and_shout(length):
  global curpos, skipsize
  tmplist = []
  for i in xrange(length):
    index = (curpos+i) % len(hashlist)
    tmplist.append(hashlist[index])
  for j, i in enumerate(tmplist[::-1]):
    index = (curpos+j) % len(hashlist)
    hashlist[index] = i
  curpos = (curpos+skipsize+length) % len(hashlist)
  skipsize += 1

def dense_hash():
  index = 0
  tmplist = []
  returnlist = []
  for i in xrange(16):
    for i in xrange(16):
      tmplist.append(hashlist[index])
      # print tmplist
      index += 1
    returnlist.append(reduce(operator.xor, tmplist))
    tmplist = []
  return returnlist

def stringify(lista):
  outstring = ''
  hexlist = map(hex, lista)
  for x in hexlist:
    x = x[2:].zfill(2)
    outstring = outstring + x
  return outstring

for _ in xrange(64):
  for length in lengths:
    twist_and_shout(length)

print stringify(dense_hash())
