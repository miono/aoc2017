#!/usr/bin/env python

class Particle:
  def __init__(self, name, position, velocity, acceleration):
    self.name = name
    self.position = position
    self.velocity = velocity
    self.acceleration = acceleration
    self.alive = 1

  def tick(self):
    self.velocity[0] += self.acceleration[0]
    self.velocity[1] += self.acceleration[1]
    self.velocity[2] += self.acceleration[2]
    self.position[0] += self.velocity[0]
    self.position[1] += self.velocity[1]
    self.position[2] += self.velocity[2]

  def get_distance(self):
    return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2]), self.name

  def get_position(self):
    return self.position, self.name

def remove_colliding(lst):
  global marked_for_deletion
  collision_coords = []
  seen_positions = []
  for i in lst:
    if i[0] in seen_positions:
      collision_coords.append(i[0])
    else:
      seen_positions.append(i[0])
  for i in lst:
    if i[0] in collision_coords:
      marked_for_deletion.append(i[1])

f = open('input').readlines()
particles = []
marked_for_deletion = []

for i, line in enumerate(f):
   line = line.strip().split(', ')
   pos = line[0][3:].rstrip('>').split(',')
   pos = map(int, pos)
   vel = line[1][3:].rstrip('>').split(',')
   vel = map(int, vel)
   acc = line[2][3:].rstrip('>').split(',')
   acc = map(int, acc)
   particles.append(Particle(i, pos, vel, acc))

for i in xrange(1000):
  remove_colliding(map(Particle.get_position, particles))
  map(Particle.tick, particles)
  print 1000 - len(marked_for_deletion)
