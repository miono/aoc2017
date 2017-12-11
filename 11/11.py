#!/usr/bin/env python

# Using even only hexgrid: http://www.roguebasin.com/index.php?title=Hexagonal_Tiles#Coordinate_systems_with_a_hex_grid

steps = open('input').readlines()[0].strip().split(',')
position = [0,0]
distances = []

def get_distance_for_point(x,y):
  x = abs(x)
  y = abs(y)
  return abs(x + (y-x)/2)

for step in steps:
  if step == 's':
    position[1] -= 2
  if step == 'n':
    position[1] += 2
  if step == 'ne':
    position[0] += 1
    position[1] += 1
  if step == 'nw':
    position[0] -= 1
    position[1] += 1
  if step == 'se':
    position[0] += 1
    position[1] -= 1
  if step == 'sw':
    position[0] -= 1
    position[1] -= 1
  distances.append(get_distance_for_point(position[0], position[1]))


print position
print get_distance_for_point(position[0], position[1])
print max(distances)
