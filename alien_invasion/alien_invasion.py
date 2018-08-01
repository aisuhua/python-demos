
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()

    # 屏幕
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 飞船
    ship = Ship(ai_settings, screen)

    # 子弹分组
    bullets = Group()

    # 外星人分组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 统计信息
    stats = GameStats(ai_settings)

    # 记分模块
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始按钮
    play_button = Button(ai_settings, screen, 'Play')

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()



