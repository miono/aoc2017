#!/usr/bin/env python

f = open('input').readlines()

registers = {
  'a' : 0,
  'b' : 0,
  'f' : 0,
  'i' : 0,
  'p' : 0
}

played_sounds = []

def int_or_reg(x):
  try:
    return int(x)
  except ValueError:
    return int(registers[x])

def my_snd(x):
  played_sounds.append(x)

def my_set(x, y):
  registers[x] = y

def my_add(x, y):
  registers[x] += y

def my_mul(x, y):
  registers[x] = registers[x] * y

def my_mod(x, y):
  registers[x] = registers[x] % y

i = 0
while True:
  if i < 0 or i >= len(f):
    break
  instr = f[i].strip().split()
  jump = 1
  if instr[0] == 'snd':
    my_snd(int_or_reg(instr[1]))
  elif instr[0] == 'set':
    my_set(instr[1], int_or_reg(instr[2]))
  elif instr[0] == 'add':
    my_add(instr[1], int_or_reg(instr[2]))
  elif instr[0] == 'mul':
    my_mul(instr[1], int_or_reg(instr[2]))
  elif instr[0] == 'mod':
    my_mod(instr[1], int_or_reg(instr[2]))
  elif instr[0] == 'jgz':
    if int_or_reg(instr[1]) > 0:
      jump = int_or_reg(instr[2])
  elif instr[0] == 'rcv':
    if int_or_reg(instr[1]) != 0:
      print played_sounds[-1]
      break
  i = i + jump

