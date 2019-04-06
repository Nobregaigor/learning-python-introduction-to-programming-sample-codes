import pygame
from pprint import pprint
import glob
from progress.bar import Bar

from classes.deck import Deck
from classes.cards import Card
from classes.player import Player
from classes.dealer import Dealer
from classes.table import Table
from classes.game import Game

def load_imgs(folder):
    files = glob.glob(folder + "/*.png")
    imgs = {}
    bar = Bar('Loading Images', max=len(files))
    for file in files:
        img_name = file.strip("imgs\\").strip(".png")
        img = pygame.image.load(file)
        img = pygame.transform.scale(img, (200, 300))
        imgs[img_name] =  img
        bar.next()
    bar.finish()
    return imgs


if __name__ == '__main__':

    pygame.init()

    #Loading
    imgs = load_imgs("imgs")

    s_heigh = 720
    s_width = 1200

    screen = pygame.display.set_mode((s_width, s_heigh))
    pygame.display.set_caption("Poker Game")


    clock = pygame.time.Clock()
    while (True):
        clock.tick(50)

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              sys.exit()

        #get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            # pygame.mixer.music.stop()
            pygame.quit()
            quit()

        # Clear the screen
        screen.fill((0, 0, 0))
        screen.blit(imgs['2C'],(0,0))
        screen.blit(imgs['4H'],(0,10))

        pygame.display.update()



    # game = Game()
    # game.build(2,['igor','bob'])
    # game.play_turn()
