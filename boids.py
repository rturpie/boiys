import math
import pygame
import math
import random

class boid():

  def get_angle(self):
    return math.atan2(self.vy,self.vx)

  def __init__(self, x, y, vx, vy, col, max_width=1000, max_height=1000):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.col = col
    self.max_width = max_width
    self.max_height = max_height

    print (max_width)
    print (max_height)

  def update_position(self,dt):
      self.x = self.x + self.vx*dt 
      self.y = self.y + self.vy*dt

      if self.x <= 0:
        self.x = self.max_width + self.x
      if self.x >= self.max_width:
        self.x = 0 

      if self.y <= 0:
        self.y = self.max_height + self.y
      if self.y >= self.max_height:
        self.y = 0

  def draw_bird(self, screen, size):
    theta = self.get_angle()
    vertex1 = [int(math.cos(theta)*size/2) + self.x, int(math.sin(theta)*size/2) + self.y]
    vertex2 = [int(math.cos(theta)*(-size/2) - math.sin(theta)*(size/4)) + self.x, int(math.sin(theta)*(-size/2) + math.cos(theta)*(size/4)) + self.y]
    vertex3 = [int(math.cos(theta)*(-size/2) - math.sin(theta)*(-size/4)) + self.x, int(math.sin(theta)*(-size/2) + math.cos(theta)*(-size/4)) + self.y]
    pygame.draw.polygon(screen, self.col , [vertex1, vertex2, vertex3], 0)

  @staticmethod
  def create_random_boids(width, height, n):
    boid_list = []
    col_lst = [(224, 254, 254), (199, 206, 234), (255, 218, 193), (255, 154, 162), (255, 255, 216), (181, 234, 215)]
    for _ in range(n):
      theta = random.random()*2*math.pi - math.pi
      col_num = random.randint(0, len(col_lst) - 1)
      print(col_num)
      boy = boid(random.randint(0,width), random.randint(0,height), 20*math.cos(theta), 20*math.sin(theta), col_lst[col_num], width, height)
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