import pygame
from pygame.sprite import Sprite
from timer import Timer


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        # initialize the ship and set its start position
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect; image from book link
        self.image = pygame.image.load('images/ship.bmp')
        self.explode_frames = ['images/ship_exp_1.bmp', 'images/ship_exp_2.bmp',
                               'images/ship_exp_3.bmp', 'images/ship_exp_4.bmp',
                               'images/ship_exp_5.bmp', 'images/ship_exp_6.bmp',
                               'images/ship_exp_7.bmp', 'images/ship_exp_8.bmp',
                               'images/ship_exp_9.bmp', 'images/ship_exp_10.bmp']
        self.timer = Timer(['images/ship.bmp'], wait=150)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for a ship's center
        self.center = float(self.rect.centerx)

        self.explode = False

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def initialize(self):
        self.explode = False
        self.image = self.image = pygame.image.load('images/ship.bmp')
        self.timer.frames = ['images/ship.bmp']
        self.timer.frameindex = 0
        self.timer.looponce = False
        self.timer.lastframe = 0
        self.timer.reset()

    def update(self):
        # update the ship's position based on the movement flags
        # update the ship's center value, not the rect
        if self.explode is False:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor

            # update rect object from self.center
            self.rect.centerx = self.center
        self.image = pygame.image.load(self.timer.imagerect())

    def blitme(self):
        # draw the ship at its current locations
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # center the ship on the screen
        self.center = self.screen_rect.centerx
