import numpy as np


class Board:

    def __init__(self):
        self.marks = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def get(self, x, y):
        return self.marks[x, y]

    def set(self, x, y, value):
        if value != 1 and value != -1:
            raise Exception('Invalid mark {} !', value)
        if self.marks[x, y] != 0:
            raise Exception('Mark already present in {},{} !', x, y)
        self.marks[x, y] = value

    def get_values(self):
        return np.array([self.marks.reshape(9,)])

    def reset(self):
        self.marks = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

