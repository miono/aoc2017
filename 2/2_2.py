#!/usr/bin/env python

import re

f = open('input')
spreadsheet = []
result_array = []

for line in f.readlines():
  spreadsheet.append(line.rstrip().split('	'))

def find_diff(arr):
  arr = map(int, arr)
  for i in arr:
    for j in xrange(len(arr)):
      if i == arr[j]:
        continue
      if i % arr[j] == 0:
        return max([i, arr[j]]) / min([i, arr[j]])


for arr in spreadsheet:
  result_array.append(find_diff(arr))

total = 0
for i in result_array:
  total += i

print total
