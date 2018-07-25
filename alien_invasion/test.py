import pygame

image = pygame.image.load('images/ship.bmp')
print(image.get_rect())

screen = pygame.display.set_mode((1200, 800))
print(screen.get_rect())
screen_rect = screen.get_rect()
print(screen_rect.centerx)
print(screen_rect.bottom)
