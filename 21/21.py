#!/usr/bin/env python

import numpy
from math import sqrt

grid = [
['.','#','.'],
['.','.','#'],
['#','#','#']
]

def str_to_array(string_grid): # Takes a string and returns an array
  square = []
  lines = string_grid.strip().split('/')
  for i in xrange(len(lines[0])):
    square.append([])
    for char in lines[i]:
      square[i].append(char)
  return square

def array_to_str(array_grid): # Takes an array and returns a string
  outstring = ''
  for line in array_grid:
    for char in line:
      outstring = outstring + char
    outstring = outstring + '/'
  outstring = outstring.rstrip('/')
  return outstring

matches = {}
def expand_matches(): # Reads the input and creates a complete, global match-dict in matches
  global matches
  f = open('arvidsinput').readlines()
  for match in f:
    in_orig, out = match.strip().split(' => ')
    in_grid = str_to_array(in_orig)
    for key in flip_n_shit(in_grid):
      matches[key] = out

def flip_n_shit(grid): # Gets one grid, and returns a list of strings that should be keys in the matches-dict
  strings = []
  m = numpy.array(grid)
  strings.append(array_to_str(m))
  strings.append(array_to_str(numpy.flipud(m)))
  strings.append(array_to_str(numpy.fliplr(m)))
  strings.append(array_to_str(numpy.fliplr(numpy.flipud(m))))
  m = numpy.rot90(m)
  strings.append(array_to_str(m))
  strings.append(array_to_str(numpy.flipud(m)))
  strings.append(array_to_str(numpy.fliplr(m)))
  strings.append(array_to_str(numpy.fliplr(numpy.flipud(m))))
  m = numpy.rot90(m)
  strings.append(array_to_str(m))
  strings.append(array_to_str(numpy.flipud(m)))
  strings.append(array_to_str(numpy.fliplr(m)))
  strings.append(array_to_str(numpy.fliplr(numpy.flipud(m))))
  m = numpy.rot90(m)
  strings.append(array_to_str(m))
  strings.append(array_to_str(numpy.flipud(m)))
  strings.append(array_to_str(numpy.fliplr(m)))
  strings.append(array_to_str(numpy.fliplr(numpy.flipud(m))))
  return strings

def get_sub_squares(grid): # Takes the whole grid and chops it up into squares
  squares = []
  if len(grid) % 2 == 0:
    square_size = 2
  if len(grid) % 3 == 0:
    square_size = 3
  square_lines = []
  for line_set in xrange(len(grid) / square_size):
    _line_set = grid[line_set * square_size : (line_set + 1) * square_size]
    for column_set in xrange(len(grid) / square_size):
      square = [line[column_set * square_size : (column_set + 1) * square_size] for line in _line_set]
      squares.append(square)
  return squares

def match_block(string_square): # Takes a string-square as argument and returns the outsquare in string-format
  return matches[string_square]
  
def assemble(squares):
  num_top_squares = int(sqrt(len(squares)))
  square_size = len(squares[0][0])
  new_grid_size = num_top_squares * square_size
  new_grid = []
  for x in xrange(new_grid_size):
    new_grid.append([])
    for y in xrange(new_grid_size):
      new_grid[x].append('')
  start_pos = [0,0]
  for i, square in enumerate(squares):
    for l, line in enumerate(square):
      for c, col in enumerate(line):
        new_grid[l + start_pos[0]][c + start_pos[1]] = col
    for i, line in enumerate(new_grid):
      try:
        j = new_grid[i].index('')
        start_pos = [i,j]
        break
      except ValueError:
        pass
  return new_grid

expand_matches()

out_sub_squares = []
for line in grid:
  print line
for i in xrange(5):
  for subsquare in get_sub_squares(grid):
    out_sub_squares.append(match_block(array_to_str(subsquare)))
  print out_sub_squares
  hej = map(str_to_array, out_sub_squares)
  grid = assemble(hej)
  out_sub_squares = []
  for line in grid:
    print line

num_hash = 0
for line in grid:
  for char in line:
    if char == '#':
      num_hash += 1

print num_hash
