import numpy as np


class GameEngine:

    def __init__(self, board):
        self.board = board
        self.current_mark = 1
        self.previous_move_outcome = 0
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0

    def get_previous_move_outcome(self):
        return self.previous_move_outcome

    def is_draw(self):
        return np.all(self.board.get_values() != 0)

    def check_if_won(self, mark):
        values = self.board.get_values()[0]
        if np.all(np.array([values[0], values[4], values[8]]) == mark):
            return True
        if np.all(np.array([values[2], values[4], values[6]]) == mark):
            return True
        if np.all(np.array([values[0], values[1], values[2]]) == mark):
            return True
        if np.all(values[0:3] == mark):
            return True
        if np.all(values[3:6] == mark):
            return True
        if np.all(values[6:9] == mark):
            return True
        if np.all(np.array([values[0], values[3], values[6]]) == mark):
            return True
        if np.all(np.array([values[1], values[4], values[7]]) == mark):
            return True
        if np.all(np.array([values[2], values[5], values[8]]) == mark):
            return True
        return False

    def make_turn(self, x, y, mark):
        if mark != self.current_mark:
            return False
        self.board.set(x, y, mark)
        self.current_mark = mark * -1
        return True

    def reset_board(self):
        self.board.reset()
        self.current_mark = 1

    def get_board(self):
        return self.board

    def game_ended(self):
        x_won = self.check_if_won(1)
        if x_won:
            self.previous_move_outcome = 1
            self.x_wins = self.x_wins + 1
        o_won = self.check_if_won(-1)
        if o_won:
            self.previous_move_outcome = -1
            self.o_wins = self.o_wins + 1

        is_draw = self.is_draw()
        if is_draw:
            self.previous_move_outcome = 0
            self.draws = self.draws + 1
        game_ended = is_draw or (x_won or o_won)
        if game_ended:
            self.reset_board()
            self.print_stats(self.x_wins, 'X')
            self.print_stats(self.o_wins, 'O')
        return game_ended

    def print_stats(self, mark, mark_char):
        total_games = self.x_wins + self.o_wins + self.draws
        print("{} wins {}%".format(mark_char, round(mark / total_games * 100, 2)))

    def get_possible_moves(self, mark):
        values = self.board.get_values()[0]
        possible_moves = []
        for idx, cell_value in enumerate(values):
            if cell_value == 0:
                new_move = values.copy()
                new_move[idx] = mark
                possible_moves.append(new_move)
        return possible_moves
