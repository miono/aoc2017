#!/usr/bin/env python

f = open('input').readlines()

registers0 = {
  'a' : 0,
  'b' : 0,
  'f' : 0,
  'i' : 0,
  'p' : 0
}

registers1 = {
  'a' : 0,
  'b' : 0,
  'f' : 0,
  'i' : 0,
  'p' : 1
}

mq_for_0 = []
mq_for_1 = []
running = 0
sent_by_1 = 0

def detect_deadlock():
  if len(mq_for_0) == 0 and len(mq_for_1) == 0:
    print "DEADLOCK"
    return True

def flip():
  global running
  if running == 0:
    running = 1
  else:
    running = 0

def int_or_reg(x):
  try:
    return int(x)
  except ValueError:
    if running == 0:
      return int(registers0[x])
    elif running == 1:
      return int(registers1[x])

def my_set(x, y):
  if running == 0:
    registers0[x] = y
  elif running == 1:
    registers1[x] = y

def my_add(x, y):
  if running == 0:
    registers0[x] += y
  elif running == 1:
    registers1[x] += y

def my_mul(x, y):
  if running == 0:
    registers0[x] = registers0[x] * y
  elif running == 1:
    registers1[x] = registers1[x] * y

def my_mod(x, y):
  if running == 0:
    registers0[x] = registers0[x] % y
  elif running == 1:
    registers1[x] = registers1[x] % y

def run_until_receiving_nothing(pos):
  global sent_by_1
  i = pos
  while True:
    if i < 0 or i >= len(f):
      print 'WEOHOHOW', running
      return i
    instr = f[i].strip().split()
    jump = 1
    if instr[0] == 'snd':
      if running == 0:
        mq_for_1.append(int_or_reg(instr[1]))
      elif running == 1:
        mq_for_0.append(int_or_reg(instr[1]))
        sent_by_1 += 1
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
      if running == 0:
        try:
          registers0[instr[1]] = mq_for_0.pop(0)
        except IndexError:
          return i
      if running == 1:
        try:
          registers1[instr[1]] = mq_for_1.pop(0)
        except IndexError:
          return i
    i = i + jump

pos0 = 0
pos1 = 0

while True:
  pos0 = run_until_receiving_nothing(pos0)
  flip()
  pos1 = run_until_receiving_nothing(pos1)
  flip()
  if detect_deadlock():
    print sent_by_1
    break
