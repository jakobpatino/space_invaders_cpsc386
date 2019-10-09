import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from text import Text
from image import Image
from high_scores import HighScores
import game_functions as gf


def run_game():
    # initialize pygame, settings, and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make play and high score button
    play_button = Button(screen, "Play", 650)
    high_score_button = Button(screen, "High Score", 700)

    # make start screen text
    title1 = Text(screen, "SPACE", screen.get_rect().centerx, 65, 500, 100,
                  (255, 255, 255), 250)
    title2 = Text(screen, "INVADERS", screen.get_rect().centerx, 175, 500,
                  100, (0, 255, 0), 158)
    high_score_title1 = Text(screen, "HIGH", (screen.get_rect().centerx - 125), 30, 180,
                             70, (255, 255, 255), 100)
    high_score_title2 = Text(screen, "SCORE", (screen.get_rect().centerx + 90), 30, 250,
                             70, (0, 255, 0), 100)
    alien_1_score = Text(screen, "= 10 PTS", (screen.get_rect().centerx + 65),
                         300, 220, 50, (255, 255, 255), 70)
    alien_2_score = Text(screen, "= 20 PTS", (screen.get_rect().centerx + 65),
                         380, 220, 50, (255, 255, 255), 70)
    alien_3_score = Text(screen, "= 40 PTS", (screen.get_rect().centerx + 65),
                         460, 220, 50, (255, 255, 255), 70)
    ufo_score = Text(screen, "= ?? PTS", (screen.get_rect().centerx + 65),
                     540, 220, 50, (255, 255, 255), 70)
    hs1 = Text(screen, "1", (screen.get_rect().centerx - 125), 100, 50, 50,
               (255, 255, 255), 65)
    hs2 = Text(screen, "2", (screen.get_rect().centerx - 125), 155, 50, 50,
               (255, 255, 255), 65)
    hs3 = Text(screen, "3", (screen.get_rect().centerx - 125), 210, 50, 50,
               (255, 255, 255), 65)
    hs4 = Text(screen, "4", (screen.get_rect().centerx - 125), 265, 50, 50,
               (255, 255, 255), 65)
    hs5 = Text(screen, "5", (screen.get_rect().centerx - 125), 320, 50, 50,
               (255, 255, 255), 65)
    hs6 = Text(screen, "6", (screen.get_rect().centerx - 125), 375, 50, 50,
               (255, 255, 255), 65)
    hs7 = Text(screen, "7", (screen.get_rect().centerx - 125), 430, 50, 50,
               (255, 255, 255), 65)
    hs8 = Text(screen, "8", (screen.get_rect().centerx - 125), 485, 50, 50,
               (255, 255, 255), 65)
    hs9 = Text(screen, "9", (screen.get_rect().centerx - 125), 540, 50, 50,
               (255, 255, 255), 65)
    hs10 = Text(screen, "10", (screen.get_rect().centerx - 125), 595, 50, 50,
                (255, 255, 255), 65)

    # make start screen images

    alien_1_img = Image(screen, 'images/alien_1_1.bmp',
                        (screen.get_rect().centerx - 150), 300)
    alien_2_img = Image(screen, 'images/alien_2_1.bmp',
                        (screen.get_rect().centerx - 150), 380)
    alien_3_img = Image(screen, 'images/alien_3_1.bmp',
                        (screen.get_rect().centerx - 150), 460)
    ufo_img = Image(screen, 'images/ufo_1.bmp',
                    (screen.get_rect().centerx - 178), 540)

    # Create an instance to store game stats and create a scoreboard
    high_scores = HighScores()
    stats = GameStats(ai_settings, high_scores)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens, and ufo group
    bullets_ship = Group()
    bullets_alien = Group()
    bunker1 = Group()
    bunker2 = Group()
    bunker3 = Group()
    aliens = Group()
    alien_type = ['images/alien_1_1.bmp', 'images/alien_1_2.bmp']
    ufo = Group()
    ufo_imgs = ['images/ufo_1.bmp', 'images/ufo_2.bmp']
    points = 10

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, stats, alien_type, points, aliens,
                    ufo_imgs, ufo)

    gf.create_bunker(screen, 1, bunker1)
    gf.create_bunker(screen, 2, bunker2)
    gf.create_bunker(screen, 3, bunker3)

    # create ship
    ship = Ship(ai_settings, screen)

    # add music
    pygame.mixer.set_reserved(0)
    pygame.mixer.set_reserved(1)
    pygame.mixer.set_reserved(2)
    pygame.mixer.set_reserved(3)
    pygame.mixer.set_reserved(4)
    pygame.mixer.set_reserved(5)
    ship_shoot = pygame.mixer.Sound('audio/ship_shoot.wav')
    alien_shoot = pygame.mixer.Sound('audio/alien_shoot.wav')
    alien_exp = pygame.mixer.Sound('audio/alien_exp.wav')
    ship_exp = pygame.mixer.Sound('audio/ship_exp.wav')
    ufo_sound = pygame.mixer.Sound('audio/ufo_sound.wav')
    pygame.mixer.music.load('audio/bg_music_1.wav')
    pygame.mixer.music.play(-1, 0.0)
    ufo_sound_playing = False

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        high_score_button, ship, aliens, alien_type, points,
                        bullets_ship, bullets_alien, bunker1, bunker2, bunker3,
                        ufo_imgs, ufo, ship_shoot)

        if stats.game_active:
            ship.update()
            if ship.timer.finished is True:
                gf.ship_hit(ai_settings, stats, screen, sb,
                            ship, aliens, alien_type, points, bullets_alien,
                            bullets_ship, high_scores, bunker1, bunker2, bunker3,
                            ufo_imgs, ufo, ship_exp)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              alien_type, points, bullets_ship, bullets_alien,
                              high_scores, bunker1, bunker2, bunker3,
                              ufo_imgs, ufo, alien_shoot, alien_exp, ship_exp)
            gf.update_aliens(ai_settings, stats, screen, sb,  ship, aliens,
                             alien_type, points, bullets_alien, bullets_ship, high_scores,
                             bunker1, bunker2, bunker3, ufo_imgs, ufo, ship_exp)

        gf.update_sound(aliens, ai_settings, stats)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets_ship, bullets_alien, play_button, high_score_button, title1,
                         title2, alien_1_score, alien_2_score, alien_3_score, ufo_score,
                         alien_1_img, alien_2_img, alien_3_img, ufo_img,
                         high_score_title1, high_score_title2, hs1, hs2, hs3,
                         hs4, hs5, hs6, hs7, hs8, hs9, hs10, high_scores, bunker1,
                         bunker2, bunker3, ufo, ufo_sound, ufo_sound_playing)


run_game()
