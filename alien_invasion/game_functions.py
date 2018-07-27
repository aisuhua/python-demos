import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, bullets, aliens, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, bullets, aliens, mouse_x, mouse_y):

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 游戏开始时隐藏鼠标
        pygame.mouse.set_visible(False)

        # 重置游戏
        stats.reset_stats()
        stats.game_active = True

        # 清空子弹和外星人
        bullets.empty()
        aliens.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event, ai_settings, screen, ship, bullets):
    ship.moving_right = False
    ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 碰撞即删
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    pygame.sprite.groupcollide(bullets, aliens, False, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

        ai_settings.increase_speed()


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        # 0/1/2/3...
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - alien_width * 2
    number_aliens_x = int(available_space_x / (alien_width * 2))

    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - ship_height - 3 * alien_height
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number

        aliens.add(alien)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检查外星人是否跟飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # 检查外星人是否触碰到底部
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):

    if stats.ships_left > 0:

        # 减少飞船数量
        stats.ships_left -= 1

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建新一批外星人，并将飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        # 游戏结束时显示鼠标
        pygame.mouse.set_visible(True)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            # why?
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()
