import pygame
import boids
import time
(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
background_colour = (13, 173, 141)
screen.fill(background_colour)
dt = 0.05

pygame.draw.polygon(screen, (244,233,222) , [[100, 100], [0, 200], [200, 200]], 5)
boid_list = boids.boid.create_random_boids(width, height, 20)



running = True
while running:
  start = time.time()
  screen.fill(background_colour)
  for boid in boid_list:
    boid.draw_bird(screen,20)
    boid.update_position(dt)
    for other_boid in boid_list:
      if not other_boid == boid:
        dist = boid.distance_to(other_boid)
        if dist <= 40:
          if abs(boid.angle_to(other_boid)) < 2.356194490192345:
            boid.draw_danger(screen)
  # tweety.draw_bird(screen,20)
  # tweety.update_position(dt)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  time.sleep(0.01)
  end = time.time()
  dt = (end - start)