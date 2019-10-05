import pickle

from view.BoardView import block_size


class Utils:

    @staticmethod
    def convert_world_local(x, y):
        coords = [int(x / block_size), int(y / block_size)]
        return coords

    @staticmethod
    def save_stats(stats):
        pickle.dump(stats, 'stats.json')

    @staticmethod
    def load_stats():
        return pickle.load('stats.json', 'rb')
