#!/usr/bin/env python

f = open('input')

pipes = f.readlines()
pipelist = []
connected_to_zero = []

for pipe in pipes:
  pipe = pipe.strip().split()
  pipelist.append([int(pipe[0]), pipe[2::]])

def check_connections(conns):
  global connected_to_zero
  for i in conns:
    i = int(i.strip(','))
    if i not in connected_to_zero:
      connected_to_zero.append(i)
      check_connections(pipelist[i][1])


check_connections(pipelist[0][1])

print len(connected_to_zero)
