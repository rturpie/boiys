import math
class boid():

  def get_angle(self):
    return math.atan2(self.vy,self.vx)

  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy

  def get_poly():
    

if __name__ == "__main__":
  boid1 = boid(0,0,1,1)
  boid2 = boid(0,0,-1,1)
  boid3 = boid(0,0,1,-1)
  boid4 = boid(0,0,-1,-1)
  print (boid1.get_angle())
  print (boid2.get_angle())
  print (boid3.get_angle())
  print (boid4.get_angle())