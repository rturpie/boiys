import math
import pygame
import math

class boid():

  def get_angle(self):
    return math.atan2(self.vy,self.vx)

  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy

  def update_position(self,dt):
      self.x = self.vx*dt 
      self.y = self.vy*dt

  def draw_bird(self, screen, size):
    theta = self.get_angle()
    vertex1 = [int(math.cos(theta)*size/2) + self.x, int(math.sin(theta)*size/2)]
    vertex2 = [int(math.cos(theta)*(-size/2) - math.sin(theta)*(size/4)) + self.x, int(math.sin(theta)*(-size/2) + math.cos(theta)*(size/4)) + self.y]
    vertex3 = [int(math.cos(theta)*(-size/2) - math.sin(theta)*(-size/4)) + self.x, int(math.sin(theta)*(-size/2) + math.cos(theta)*(-size/4)) + self.y]
    pygame.draw.polygon(screen, (244,233,222) , [vertex1, vertex2, vertex3], 5)




    

if __name__ == "__main__":
  boid1 = boid(0,0,1,1)
  boid2 = boid(0,0,-1,1)
  boid3 = boid(0,0,1,-1)
  boid4 = boid(0,0,-1,-1)
  print (boid1.get_angle())
  print (boid2.get_angle())
  print (boid3.get_angle())
  print (boid4.get_angle())