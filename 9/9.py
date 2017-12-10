#!/usr/bin/env python

f = open('input').readlines()[0]
total = 0
garbage = False
skip = False
level = 1 
garbage_count = 0

for char in f:
  if not garbage:
    if char == '<':
      garbage = True
    elif char == '{':
      total += level
      level += 1
    elif char == '}':
      level -= 1
  else:
    if skip:
      skip = False
    elif char == '!':
      skip = True
    elif char == '>':
      garbage = False
    else:
      garbage_count += 1

print garbage_count
print total
