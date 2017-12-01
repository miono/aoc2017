#!/usr/bin/env python

f = str(open('input2').readlines()[0].rstrip())
summable = []
# 
# print f[0][0]
# print f
# 
# print len(f)
# for position in xrange(len(f)):
#   if f[position] == f[position - 1]:
#     summable.append(f[position])
# 
# total = 0
# for i in summable:
#   total += int(i)
# 
# 
# print total
# 

print len(f)

for i in xrange(2110):
  if f[i] == f[i + 1055]:
    print summable
    summable.append(f[i])

total = 0
for i in summable:
  total += int(i)

print total
