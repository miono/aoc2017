#!/usr/bin/env python

class Particle:
  def __init__(self, name, position, velocity, acceleration):
    self.name = name
    self.position = position
    self.velocity = velocity
    self.acceleration = acceleration

  def tick(self):
    self.velocity[0] += self.acceleration[0]
    self.velocity[1] += self.acceleration[1]
    self.velocity[2] += self.acceleration[2]
    self.position[0] += self.velocity[0]
    self.position[1] += self.velocity[1]
    self.position[2] += self.velocity[2]

  def get_distance(self):
    return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2]), self.name

f = open('input').readlines()
particles = []

for i, line in enumerate(f):
  line = line.strip().split(', ')
  pos = line[0][3:].rstrip('>').split(',')
  pos = map(int, pos)
  vel = line[1][3:].rstrip('>').split(',')
  vel = map(int, vel)
  acc = line[2][3:].rstrip('>').split(',')
  acc = map(int, acc)
  particles.append(Particle(i, pos, vel, acc, 0))

for i in xrange(5000):
  map(Particle.tick, particles)

print min(map(Particle.get_distance, particles))
