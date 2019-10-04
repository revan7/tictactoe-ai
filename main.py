import logging
import traceback

from engine.GameEngine import *
from engine.player.AIPlayer import AIPlayer
from model.Board import Board
from engine.player.HumanPlayer import HumanPlayer
from view.BoardView import *

pygame.init()
clock = pygame.time.Clock()


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
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
            clock.tick(1000)
        except Exception:
            traceback.print_exc()


def print_stats(x_wins, o_wins, draw):
    all_games = x_wins + o_wins + draw
    print("Times X won: {}", x_wins / all_games)


if __name__ == '__main__':
    main()

pygame.quit()
