#!/usr/bin/env python

f = open('input').readlines()
lines = []
num_ones = 0

for line in f:
  lines.append(line.strip())

def get_binary_hash(hexhash):
  outstring = ''
  for char in hexhash:
    outstring = outstring + str(bin(int(char, 16)))[2:].zfill(4)
  return outstring

for hexhash in lines:
  binhash = get_binary_hash(hexhash)
  for char in binhash:
    if char == '1':
      num_ones += 1

print num_ones
