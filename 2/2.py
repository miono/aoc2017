#!/usr/bin/env python

import re

f = open('input')
spreadsheet = []
result_array = []

for line in f.readlines():
  spreadsheet.append(line.rstrip().split('	'))

def find_diff(arr):
  arr = map(int, arr)
  return max(arr) - min(arr)

for arr in spreadsheet:
  # print arr
  result_array.append(find_diff(arr))

total = 0
for i in result_array:
  total += i

print total
