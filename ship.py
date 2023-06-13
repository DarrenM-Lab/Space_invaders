import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self,ai_game):
        super().__init__()
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images\spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.width/2

        self.x = float(self.rect.x)

        # Start each new ship at the bottom center of the screen
        
        self.rect.midbottom = self.screen_rect.midbottom 
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.rect.x = self.screen_rect.width/2
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)