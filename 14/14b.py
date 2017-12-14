#!/usr/bin/env python

f = open('input').readlines()
lines = []
grid = [[0 for i in xrange(128)] for j in xrange(128)]
index_num = 1

for line in f:
  lines.append(line.strip())

def get_binary_hash(hexhash):
  outstring = ''
  for char in hexhash:
    outstring = outstring + str(bin(int(char, 16)))[2:].zfill(4)
  return outstring

def resolve_group(i, j):
  global index_num
  members = []
  grid[i][j] = index_num
  members.append([i, j])
  try:
    if grid[i-1][j] == '#' and [i-1, j] not in members and i != 0:
      grid[i-1][j] = index_num
      members.append([i-1, j])
      resolve_group(i-1, j)
  except IndexError:
    pass
  try:
    if grid[i+1][j] == '#' and [i+1, j] not in members:
      grid[i+1][j] = index_num
      members.append([i+1, j])
      resolve_group(i+1, j)
  except IndexError:
    pass
  try:
    if grid[i][j-1] == '#' and [i, j-1] not in members and j != 0:
      grid[i][j-1] = index_num
      members.append([i, j-1])
      resolve_group(i, j-1)
  except IndexError:
    pass
  try:
    if grid[i][j+1] == '#' and [i, j+1] not in members:
      grid[i][j+1] = index_num
      members.append([i, j+1])
      resolve_group(i, j+1)
  except IndexError:
    pass

for i, hexhash in enumerate(lines):
  binhash = get_binary_hash(hexhash)
  for j, char in enumerate(binhash):
    if char == '1':
      grid[i][j] = '#'
    else:
      grid[i][j] = 0

for i in xrange(128):
  for j in xrange(128):
    if grid[i][j] == '#':
      resolve_group(i, j)
      index_num += 1

for line in grid:
  print max(line)
