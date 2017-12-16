#!/usr/bin/env python

steps = open('input').readlines()[0].strip().split(',')

dancers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
# dancers = ['a', 'b', 'c', 'd', 'e']

def spin(x):
  global dancers
  new_beginning = dancers[-x:]
  the_end = dancers[:-x]
  dancers = []
  for dancer in new_beginning:
    dancers.append(dancer)
  for dancer in the_end:
    dancers.append(dancer)

def exchange(x, y):
  global dancers
  exchange_x = dancers[x]
  exchange_y = dancers[y]
  dancers[x] = exchange_y
  dancers[y] = exchange_x

def partner(x, y):
  global dancers
  index_x = dancers.index(x)
  index_y = dancers.index(y)
  new_x_val = dancers[dancers.index(y)]
  new_y_val = dancers[dancers.index(x)]
  dancers[index_x] = new_x_val
  dancers[index_y] = new_y_val

for step in steps:
  if step[0] == 's':
    spin(int(step[1:]))
  elif step[0] == 'p':
    partner(step[1], step[3])
  elif step[0] == 'x':
    tmp_list = step.split('/')
    exchange(int(tmp_list[0][1:]), int(tmp_list[1]))

print ''.join(dancers)
