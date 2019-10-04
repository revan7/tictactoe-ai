import unittest

from src.model.Board import Board


class BoardTest(unittest.TestCase):

    def test_invalid_mark(self):
        board = Board()
        board.set(1, 1, 1)
        with self.assertRaises(Exception):
            board.set(1, 2, 6)

    def test_mark_already_present(self):
        board = Board()
        board.set(1, 1, 1)
        with self.assertRaises(Exception):
            board.set(1, 1, 1)