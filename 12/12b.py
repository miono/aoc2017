#!/usr/bin/env python

pipes = open('input').readlines()

pipelist, tmpgroup, groups, touched_pipes = [], [], [], []

for pipe in pipes:
  pipe = pipe.strip().split()
  pipelist.append([int(pipe[0]), pipe[2::]])

def check_connections(conns):
  global tmpgroup, touched_pipes
  for i in conns:
    i = int(i.strip(','))
    if i not in tmpgroup:
      tmpgroup.append(i)
      touched_pipes.append(i)
      check_connections(pipelist[i][1])

for i in xrange(len(pipelist)):
  if i not in touched_pipes:
    check_connections(pipelist[i][1])
    groups.append(tmpgroup)
    tmpgroup = []

print len(groups)
