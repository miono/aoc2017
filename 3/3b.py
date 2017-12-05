#!/usr/bin/env python

matrix = [[0 for i in xrange(50)] for j in xrange(50)] # Create a big enough matrix
mover = [len(matrix) / 2 ,len(matrix) / 2,'e'] # Center the mover in the matrix
matrix[mover[0]][mover[1]] = 1

def getvalue(x, y):
  total = 0
  total += matrix[x - 1][y]
  total += matrix[x + 1][y]
  total += matrix[x][y - 1]
  total += matrix[x][y + 1]
  total += matrix[x - 1][y + 1]
  total += matrix[x - 1][y - 1]
  total += matrix[x + 1][y - 1]
  total += matrix[x + 1][y + 1]
  return total


def fill_matrix_until(n):
  moveamount = 1
  while True:
    for i in xrange(2):
      if mover[2] == 'e':
        for j in xrange(moveamount):
          mover[0] += 1
          bit = getvalue(mover[0], mover[1])
          if bit > n:
            return bit
          else:
            matrix[mover[0]][mover[1]] = bit
      if mover[2] == 'w':
        for j in xrange(moveamount):
          mover[0] -= 1
          bit = getvalue(mover[0], mover[1])
          if bit > n:
            return bit
          else:
            matrix[mover[0]][mover[1]] = bit
      if mover[2] == 'n':
        for j in xrange(moveamount):
          mover[1] += 1
          bit = getvalue(mover[0], mover[1])
          if bit > n:
            return bit
          else:
            matrix[mover[0]][mover[1]] = bit
      if mover[2] == 's':
        for j in xrange(moveamount):
          mover[1] -= 1
          bit = getvalue(mover[0], mover[1])
          if bit > n:
            return bit
          else:
            matrix[mover[0]][mover[1]] = bit
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

print fill_matrix_until(312051)
