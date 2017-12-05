#!/usr/bin/env python

mover = [0,0,'e']

def getcoordsforbit(n):
  bit = 1
  moveamount = 1
  while bit != n:
    for i in xrange(2):
      if mover[2] == 'e':
        for j in xrange(moveamount):
          mover[0] += 1
          bit += 1
          if bit == n:
            return
      if mover[2] == 'w':
        for j in xrange(moveamount):
          mover[0] -= 1
          bit += 1
          if bit == n:
            return
      if mover[2] == 'n':
        for j in xrange(moveamount):
          mover[1] += 1
          bit += 1
          if bit == n:
            return
      if mover[2] == 's':
        for j in xrange(moveamount):
          mover[1] -= 1
          bit += 1
          if bit == n:
            return
      turn()
    moveamount += 1
    

def turn():
  if mover[2] == 'e':
    mover[2] = 'n'
    return
  if mover[2] == 'n':
    mover[2] = 'w'
    return
  if mover[2] == 'w':
    mover[2] = 's'
    return
  if mover[2] == 's':
    mover[2] = 'e'
    return
