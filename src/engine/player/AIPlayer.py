from engine.AI.ThompsonSampling import ThompsonSampling
from model.Player import Player


class AIPlayer(Player):

    def __init__(self, mark, name, engine, model='thompson-sampling'):
        if model == 'thompson-sampling':
            self.model = ThompsonSampling(mark, engine)
        Player.__init__(self, mark, name, engine)

    def make_move(self):
        row, col = self.model.make_move()
        self.engine.make_turn(row, col, self.mark)

    def key(self, arr):
        return ''.join(map(str, arr))
