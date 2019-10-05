import os
import pickle
import random

from model.Stats import Stats


class ThompsonSampling:

    def __init__(self, mark, engine):
        self.mark = mark
        self.engine = engine
        self.stats = Stats()
        self.last_move_key = ''
        self.number_of_rewards_1 = {} if not os.path.isfile('nor1.save') else pickle.load(open('nor1.save', 'rb'))
        self.number_of_rewards_0 = {} if not os.path.isfile('nor0.save') else pickle.load(open('nor0.save', 'rb'))

    def make_move(self):
        values = self.engine.get_board().get_values()[0]
        possible_moves = self.engine.get_possible_moves(self.mark)
        next_move = []
        max_random = 0
        for i in range(0, len(possible_moves)):
            previous_move_outcome = self.engine.get_previous_move_outcome()
            possible_move_key = self.key(possible_moves[i])
            if possible_move_key not in self.number_of_rewards_1:
                self.number_of_rewards_1[possible_move_key] = 0
            if possible_move_key not in self.number_of_rewards_0:
                self.number_of_rewards_0[possible_move_key] = 0
            reward = 0.5
            if previous_move_outcome == self.mark:
                reward = 1
            if previous_move_outcome == self.mark * -1:
                reward = 0
            if self.last_move_key:
                if reward == 0:
                    self.number_of_rewards_0[self.last_move_key] = self.number_of_rewards_0[self.last_move_key] + 1
                else:
                    self.number_of_rewards_1[self.last_move_key] = self.number_of_rewards_1[self.last_move_key] + reward
            random_beta = random.betavariate(self.number_of_rewards_1[possible_move_key] + 1,
                                             self.number_of_rewards_0[possible_move_key] + 1)
            if random_beta > max_random:
                max_random = random_beta
                next_move = possible_moves[i]
        move_index = 0
        self.last_move_key = self.key(next_move)
        for i in range(0, 9):
            if values[i] != next_move[i]:
                move_index = i
        row = int(move_index / 3)
        col = move_index % 3
        self.stats.increment_iteration()
        if self.stats.get_iterations() % 10000 == 0:
            pickle.dump(self.number_of_rewards_1, open('nor1.save', 'wb'))
            pickle.dump(self.number_of_rewards_0, open('nor0.save', 'wb'))
        return row, col

    def key(self, arr):
        return ''.join(map(str, arr))
