#!/usr/bin/env python

grid = [[0 for i in xrange(200)] for j in xrange(200)]
f = open('input').readlines()
outstring = []
pos_x = 0
pos_y = 19
steps = 0
direction = 's'

for x, line in enumerate(f):
  line = line.rstrip('\n')
  for y, char in enumerate(line):
    grid[x][y] = char

def turn(pos_x, pos_y, direction):
  if direction == 's':
    if grid[pos_x][pos_y-1] not in [' ', '|']:
      return 'w'
    if grid[pos_x][pos_y+1] not in [' ', '|']:
      return 'e'
  if direction == 'n':
    if grid[pos_x][pos_y-1] not in [' ', '|']:
      return 'w'
    if grid[pos_x][pos_y+1] not in [' ', '|']:
      return 'e'
  if direction == 'w':
    if grid[pos_x-1][pos_y] not in [' ', '-']:
      return 'n'
    if grid[pos_x+1][pos_y] not in [' ', '-']:
      return 's'
  if direction == 'e':
    if grid[pos_x-1][pos_y] not in [' ', '-']:
      return 'n'
    if grid[pos_x+1][pos_y] not in [' ', '-']:
      return 's'

while True:
  if grid[pos_x][pos_y] == '+':
    direction = turn(pos_x, pos_y, direction)
  if grid[pos_x][pos_y] not in ['+', '-', '|']:
    outstring.append(grid[pos_x][pos_y])

  if direction == 's':
    pos_x += 1
  if direction == 'n':
    pos_x -= 1
  if direction == 'w':
    pos_y -= 1
  if direction == 'e':
    pos_y += 1

  steps += 1

  if grid[pos_x][pos_y] == ' ':
    break

print ''.join(outstring)
print steps
