import pygame
import boids

(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
background_colour = (255,182,193)
screen.fill(background_colour)

pygame.draw.polygon(screen, (244,233,222) , [[100, 100], [0, 200], [200, 200]], 5)

tweety = boids.boid(100,200,5,5)

tweety.draw_bird(screen,20)

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False