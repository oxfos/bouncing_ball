class Settings:
    """
    Class to define game's settings
    """

    def __init__(self):
        """We initialize the game with some settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,255)
        # Bar speed
        self.bar_speed = 10
        # Ball settings
        self.ball_speed = 5
        self.ball_width = 20
        self.ball_height = 20
        self.ball_color = (255,255,255)