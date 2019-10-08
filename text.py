import pygame.font


class Text:

    def __init__(self, screen, msg, centerx, recty, width, height, color, size):
        # initialize text attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the text rect
        self.width, self.height = width, height
        self.button_color = (0, 255, 233)
        self.text_color = color
        self.font = pygame.font.SysFont(None, size)

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = centerx
        self.rect.y = recty

        # the button message needs to be prepped only once
        self.msg_image = None
        self.msg_image_rect = None
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_text(self):
        # draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
