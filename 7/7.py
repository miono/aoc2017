#!/usr/bin/env python

f = open('input').readlines()
towerlist = []

for i in f:
  towerdef = i.split()
  if len(towerdef) > 2:
    tmplist = [towerdef[0], towerdef[1], towerdef[3:]]
  else:
    tmplist = [towerdef[0], towerdef[1]]
  towerlist.append(tmplist)

for tower in towerlist:
  for inner in tower:
    if type(inner) is list:
      for j in inner:
        print j
    else:
      print inner

