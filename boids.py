import math
import pygame
import math
import random
from constants import *

class boid():

  def get_angle(self):
    return math.atan2(self.vy,self.vx)

  def __init__(self, x, y, vx, vy, col=(0,0,0), WIDTH=1000, HEIGHT=1000):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.ax = 0
    self.ay = 0
    self.col = col

  def update_position(self,dt):
    # apply forces
    self.vx += self.ax
    self.vy += self.ay

    # limit speed
    v_abs = math.sqrt(self.vx * self.vx + self.vy * self.vy)
    if (v_abs) > SPEED:
      self.vx = self.vx / v_abs * SPEED
      self.vy = self.vy / v_abs * SPEED

    # update positions
    self.x = self.x + self.vx*dt 
    self.y = self.y + self.vy*dt

    # loop out of bounds
    self.x = self.x % WIDTH
    self.y = self.y % HEIGHT

  def draw_danger(self, screen):
    """
    display detection of nearby boids
    """
    if DEBUG:
      pygame.draw.circle(screen, (255, 0, 0, 1), (int(self.x), int(self.y)), 40, 1)

  def distance_to(self, bd):
    """
    Get the euclidean distance to a given boid bd
    """
    return math.sqrt((bd.x - self.x)**2 + (bd.y - self.y)**2)

  def angle_to(self, bd):
    """
    Get the angle to a given boid relative to current direction
    """
    return self.get_angle() - math.atan2(bd.y-self.y, bd.x-self.x)

  def draw_bird(self, screen):
    theta = self.get_angle()

    # Apply matrix rotation by theta to triangle points
    vertex1 = [int(math.cos(theta)*BOID_SIZE/2) + self.x, int(math.sin(theta)*BOID_SIZE/2) + self.y]
    vertex2 = [int(math.cos(theta)*(-BOID_SIZE/2) - math.sin(theta)*(BOID_SIZE/4)) + self.x, int(math.sin(theta)*(-BOID_SIZE/2) + math.cos(theta)*(BOID_SIZE/4)) + self.y]
    vertex3 = [int(math.cos(theta)*(-BOID_SIZE/2) - math.sin(theta)*(-BOID_SIZE/4)) + self.x, int(math.sin(theta)*(-BOID_SIZE/2) + math.cos(theta)*(-BOID_SIZE/4)) + self.y]
    
    # Draw filled boid
    pygame.draw.polygon(screen, self.col , [vertex1, vertex2, vertex3], 0)

  @staticmethod
  def create_random_boids(n):
    boid_list = []
    col_lst = [(224, 254, 254), (199, 206, 234), (255, 218, 193), (255, 154, 162), (255, 255, 216), (181, 234, 215)]
    for _ in range(n):
      theta = random.random()*2*math.pi - math.pi
      col_num = random.randint(0, len(col_lst) - 1)
      boy = boid(random.randint(0,WIDTH), random.randint(0,HEIGHT), SPEED*math.cos(theta), SPEED*math.sin(theta), col_lst[col_num], WIDTH, HEIGHT)
      boid_list.append(boy)
    return boid_list

if __name__ == "__main__":
  boid1 = boid(0,0,1,1)
  boid2 = boid(0,0,-1,1)
  boid3 = boid(0,0,1,-1)
  boid4 = boid(0,0,-1,-1)
  print (boid1.get_angle())
  print (boid2.get_angle())
  print (boid3.get_angle())
  print (boid4.get_angle())