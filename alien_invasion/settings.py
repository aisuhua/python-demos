
class Settings():
    def __init__(self):

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 50

        # 提速的速率
        self.speedup_scale = 1.1

        # 分数随游戏速度加快而递增倍数
        self.score_scale = 1.5

        # 更新动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """更新动态配置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1
        # 击落外星人所得分数
        self.alien_points = 50

    def increase_speed(self):
        """加快游戏速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # 游戏速度加快后，得分相应增加
        self.alien_points = int(self.alien_points * self.score_scale)
