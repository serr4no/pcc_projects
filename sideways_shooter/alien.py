import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Intitializes the alien and set its starting positions."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alient image and set its rect attribute.
        self.image = pygame.image.load('sideways_shooter/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien as at the edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= screen_rect.top)

    def update(self):
        """Move the alien right or left."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y