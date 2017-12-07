#!/usr/bin/env python

f = open('input').readlines()
towerlist = []
resolved_tower = []

for i in f:
  towerdef = i.split()
  if len(towerdef) > 2:
    tmplist = [towerdef[0], int(towerdef[1].strip('()')), map(lambda it: it.strip(','), towerdef[3:])]
  else:
    tmplist = [towerdef[0], int(towerdef[1].strip('()'))]
  towerlist.append(tmplist)


# Resolve tower
# resolved_tower.append(['dgoocsw', 99, ['ifajhb', 'gqmls', 'sgmbw', 'ddkhuyg', 'rhqocy']])

def resolve(tower):
  towerdef = []
  #Find towerdef
  for towerdef in towerlist:
    if towerdef[0] == tower:
      tmpweight = towerdef[1]
      resolved_tower.append([tower, tmpweight])
      print [tower, tmpweight]
      break
  if len(towerdef) == 2:
    return 1
  for subtower in towerdef[2]:
    resolve(subtower)

weight = 0
def get_full_weight(tower):
  global weight
  towerdef = []
  #Find towerdef
  for towerdef in towerlist:
    if towerdef[0] == tower:
      weight += towerdef[1]
      # print weight
      break
  if len(towerdef) == 2:
    return 1
  for subtower in towerdef[2]:
    get_full_weight(subtower)

# resolve('dgoocsw')
get_full_weight('ifajhb')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('gqmls')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('sgmbw')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('ddkhuyg')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('rhqocy')
print weight
weight = 0
print '#########'
get_full_weight('fqvvrgx')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('szmnwnx')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('jfdck')
print weight
weight = 0
print '%%%%%%%%%'
print '##########'
get_full_weight('marnqj')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('moxiw')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('sxijke')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('ojgdow')
print weight
weight = 0
print '%%%%%%%%%'
get_full_weight('fnlapoh')
print weight
weight = 0
print '%%%%%%%%%'
print '#############'
get_full_weight('upair')
print weight
weight = 0
get_full_weight('mkrrlbv')
print weight
weight = 0
get_full_weight('vqkwlq')
print weight
weight = 0
get_full_weight('wsrmfr')
print weight
weight = 0
