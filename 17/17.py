#!/usr/bin/env pypy

step = 363
length_of_list = 1
curpos = 0
val = 0

for i in xrange(50000000):
  next_pos = (curpos + step) % length_of_list
  if next_pos == 0:
    val = i+1
  length_of_list += 1
  curpos = next_pos + 1

print val
