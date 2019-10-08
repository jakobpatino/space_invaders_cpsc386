import pygame
from pygame.sprite import Sprite


class Bunker(Sprite):
    # a class to represent a single alien in the fleet

    def __init__(self, screen, frames, top, left):
        # initialize the alien and set its start position
        super(Bunker, self).__init__()
        self.screen = screen
        self.hits = 0
        self.frame = 0
        self.frames = frames

        # load the bunker image and set its rect attribute
        self.image = None
        self.initialize()
        self.rect = self.image.get_rect()

        # spawn bunker at assigned location
        self.rect.top = top
        self.rect.left = left

    #def blitme(self):
    #    # draw the alien at its current position
    #    self.screen.blit(self.image, self.rect)

    def update(self):
        # swap image
        self.image = pygame.image.load(self.frames[1])

    def initialize(self):
        self.image = pygame.image.load(self.frames[0])