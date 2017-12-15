#!/usr/bin/env python

a_factor = 16807
b_factor = 48271

a_val = 618
b_val = 814

times = 0
matches = 0

for i in xrange(40000000):
  a_val = (a_val * a_factor) % 2147483647
  b_val = (b_val * b_factor) % 2147483647
  if bin(a_val)[-16:] == bin(b_val)[-16:]:
    matches += 1

print matches
