import sys

import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_event(event, ship):
    ship.moving_right = False
    ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
