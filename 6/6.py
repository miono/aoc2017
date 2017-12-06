#!/usr/bin/env python

f = open('input').readlines()[0]
f = f.split('	')
cur_bank = map(int, f)

all_results = []
all_results.append(cur_bank)

def redistribute(bank_config):
  m = max(bank_config)
  bank_to_distribute = [i for i, j in enumerate(bank_config) if j == m][0]
  num_steps = bank_config[bank_to_distribute]
  bank_config[bank_to_distribute] = 0
  for x in xrange(num_steps):
    bank_config[(bank_to_distribute + x + 1) % len(bank_config)] += 1
  if bank_config in all_results:
    print "Number of cycles before loop: %i" % (len(all_results))
    print "Loop-length: %i" % (len(all_results) - all_results.index(bank_config))
    exit()
  return bank_config

while True:
  all_results.append(redistribute(list(all_results[-1])))
