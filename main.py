import pygame
import boids
import time
from constants import WIDTH, HEIGHT, BACKGROUND_COLOUR

# create pygame screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create list of n boids
boid_list = boids.boid.create_random_boids(20)

running = True
dt = 1
while running:
  start = time.time()

  # Set background / refresh canvas
  screen.fill(BACKGROUND_COLOUR)

  # Update and draw boids
  for boid in boid_list:
    boid.draw_bird(screen)
    boid.update_position(dt)
    for other_boid in boid_list:
      if not other_boid == boid:
        dist = boid.distance_to(other_boid)
        if dist <= 40:
          if abs(boid.angle_to(other_boid)) < 2.356194490192345:
            boid.draw_danger(screen)

  # Check for window close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Draw to screem
  pygame.display.flip()

  # Update dt
  time.sleep(0.01)
  end = time.time()
  dt = (end - start)