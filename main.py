import pygame

(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
background_colour = (255,182,193)
screen.fill(background_colour)
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False