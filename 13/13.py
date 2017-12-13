#!/usr/bin/env python

f = open('input').readlines()
severity = 0

for line in f:
  second = int(line.strip().split(': ')[0])
  scanrange = int(line.strip().split(': ')[1])
  looplength = (scanrange - 1) * 2
  if second % looplength == 0:
    print second, scanrange
    severity = severity + (second * scanrange)

print severity
