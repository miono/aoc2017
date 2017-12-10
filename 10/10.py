#!/usr/bin/env python

f = open('input').readlines()[0].strip().split(',')

hashlist = [i for i in xrange(256)]
curpos = 0
skipsize = 0

def twist_and_shout(length):
  global curpos, skipsize
  tmplist = []
  for i in xrange(length):
    index = (curpos+i) % len(hashlist)
    tmplist.append(hashlist[index])
  for j, i in enumerate(tmplist[::-1]):
    index = (curpos+j) % len(hashlist)
    hashlist[index] = i
  curpos = (curpos+skipsize+length) % len(hashlist)
  skipsize += 1

for length in f:
  twist_and_shout(int(length))
  

print hashlist
print curpos
print skipsize
