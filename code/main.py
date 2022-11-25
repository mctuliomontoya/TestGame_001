import pygame as pg
import sys
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.setmode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            pg.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
