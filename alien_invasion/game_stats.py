
class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings

        # 飞船剩余数量
        self.ships_left = self.ai_settings.ship_limit

        # 游戏是否已经开始
        self.game_active = False

        # 游戏得分
        self.score = 0
        # 最高得分
        self.high_score = 0
        # 玩家等级
        self.level = 1

        # 重置游戏信息
        self.reset_stats()

    def reset_stats(self):
        """重置游戏参数"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
