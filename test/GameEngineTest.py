import unittest

import numpy as np
import logging
from src.engine.GameEngine import GameEngine
from src.model.Board import Board

logger = logging.getLogger()


class GameEngineTest(unittest.TestCase):

    def test_board_doesnt_have_blanks(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.is_draw())
        self.fill_board(board, np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
        self.assertTrue(engine.is_draw())

    def test_victory_cross_1(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertTrue(engine.check_if_won(1))

    def test_victory_cross_2(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]))
        self.assertTrue(engine.check_if_won(1))

    def test_victory_cross_3(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]))
        self.assertTrue(engine.check_if_won(1))

    def test_victory_cross_4(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]]))
        self.assertTrue(engine.check_if_won(1))

    def test_victory_cross_5(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]]))
        self.assertTrue(engine.check_if_won(1))

    def test_victory_cross_6(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[0, -1, 1], [-1, 1, 0], [1, 0, -1]]))
        self.assertTrue(engine.check_if_won(1))

    def test_victory_cross_7(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[0, 0, 1], [0, 1, 1], [0, 0, 1]]))
        self.assertTrue(engine.check_if_won(1))

    def test_victory_cross_8(self):
        board = Board()
        engine = GameEngine(board)
        self.assertFalse(engine.check_if_won(1))
        self.fill_board(board, np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]))
        self.assertTrue(engine.check_if_won(1))

    def test_draw(self):
        board = Board()
        engine = GameEngine(board)
        self.fill_board(board, np.array([1, -1, 1], [-1, 1, -1], [1, -1, 1]))
        self.assertTrue(engine.is_draw())

    def fill_board(self, board, values):
        for i in range(0, 3):
            for j in range(0, 3):
                mark = values[i, j]
                if mark != 0:
                    board.set(i, j, mark)