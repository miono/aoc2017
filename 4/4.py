#!/usr/bin/env python

from collections import Counter

f = open('input')
valid = 0

for line in f.readlines():
  line = line.rstrip()
  words = line.split(' ')
  sorted_words = []
  for word in words:
    h = sorted(word)
    j = "".join(h)
    sorted_words.append(j)
  print Counter(sorted_words)
