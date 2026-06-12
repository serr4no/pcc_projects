class Settings:
    """"A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initializae the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.rocket_speed = 1.5
        self.rocket_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right; -1 represents left
        self.fleet_direction = 1