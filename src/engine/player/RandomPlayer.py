from model.Player import Player
import logging
import random

class RandomPlayer(Player):

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    def make_move(self):
        done = self.engine.is_draw()
        while not done:
            try:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
                self.engine.make_turn(x, y, self.mark)
                done = True
            except Exception as e:
                pass
