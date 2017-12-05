#!/usr/bin/env python

f = open('input')

jumplist = f.readlines()

jumplist = map(int, jumplist)

steps = 0
index = 0


while True:
  try:
    jump = jumplist[index]
    if jumplist[index] >= 3:
      jumplist[index] -= 1
    else:
      jumplist[index] += 1
    index = index + jump
    steps += 1
  except IndexError:
    print steps
    break
