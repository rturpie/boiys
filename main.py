import pygame
import boids

(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
background_colour = (255,182,193)
screen.fill(background_colour)
dt = 0.05

pygame.draw.polygon(screen, (244,233,222) , [[100, 100], [0, 200], [200, 200]], 5)

tweety = boids.boid(100,200,20,20, width, height)

tweety.draw_bird(screen,20)

boid_list = boids.boid.create_random_boids(width, height, 20)



running = True
while running:
  screen.fill(background_colour)
  for boid in boid_list:
    boid.draw_bird(screen,20)
    boid.update_position(dt)
  tweety.draw_bird(screen,20)
  tweety.update_position(dt)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False