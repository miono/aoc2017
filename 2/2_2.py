#!/usr/bin/env python

f = open('input')
spreadsheet = []
result_array = []

for line in f.readlines():
  spreadsheet.append(line.rstrip().split('	'))

def find_diff(arr):
  arr = map(int, arr)
  for i in arr:
    for j in arr:
      if i == j:
        continue
      if i % j == 0:
        return max([i, j]) / min([i, j])


for arr in spreadsheet:
  result_array.append(find_diff(arr))

total = 0
for i in result_array:
  total += i

print total
