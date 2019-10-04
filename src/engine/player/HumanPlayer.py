import sys

import pygame

from engine.Utils import Utils
from model.Player import Player
pygame.init()
clock = pygame.time.Clock()


class HumanPlayer(Player):

    def make_move(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    click_coord = event.pos
                    coords = Utils.convert_world_local(click_coord[0], click_coord[1])
                    self.engine.make_turn(coords[1], coords[0], self.mark)
                    done = True
