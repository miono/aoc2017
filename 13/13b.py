#!/usr/bin/env python

f = open('input').readlines()
delay = 0 

fw = []
for line in f:
  fw.append([int(line.strip().split(': ')[0]), int(line.strip().split(': ')[1])])

def gogogo(delay):
  severity = 0
  for pair in fw:
    second = pair[0]+ delay
    scanrange = pair[1]
    looplength = (scanrange - 1) * 2
    if second % looplength == 0:
      severity = severity + (second * scanrange)
      if severity > 0:
        break
  return severity

while True:
  if gogogo(delay) == 0:
    print delay
    break
  delay += 1
