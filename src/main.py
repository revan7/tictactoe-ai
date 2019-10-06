import logging
import traceback

from engine.GameEngine import *
from engine.player.AIPlayer import AIPlayer
from engine.player.HumanPlayer import HumanPlayer
from engine.player.RandomPlayer import RandomPlayer
from model.Board import Board
from view.BoardView import *

pygame.init()
clock = pygame.time.Clock()


def main():
    board = Board()
    engine = GameEngine(board)
    player = AIPlayer(1, "dude", engine)
    random_player = HumanPlayer(-1, "Rand", engine)
    view = BoardView(board)
    done = False
    view.update()
    while not done:
        try:
            player.make_move()
            view.update()
            if engine.game_ended():
                view.reset()
                continue
            random_player.make_move()
            view.update()
            if engine.game_ended():
                view.reset()
                continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    main()

pygame.quit()
