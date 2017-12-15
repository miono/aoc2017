#!/usr/bin/env python

a_factor = 16807
b_factor = 48271

a_val = 618
b_val = 814

times = 0
matches = 0

def get_new_a(last_val):
  global a_val, a_factor
  a_val = (last_val * a_factor) % 2147483647
  while a_val % 4 != 0:
    a_val = (a_val * a_factor) % 2147483647
  return a_val

def get_new_b(last_val):
  global b_val, b_factor
  b_val = (last_val * b_factor) % 2147483647
  while b_val % 8 != 0:
    b_val = (b_val * b_factor) % 2147483647
  return b_val

 
for i in xrange(5000000):
  a_val = get_new_a(a_val)
  b_val = get_new_b(b_val)
  if bin(a_val)[-16:] == bin(b_val)[-16:]:
    matches += 1

print matches
