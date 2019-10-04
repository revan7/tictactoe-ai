import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (500, 500)
line_width = 4
block_size = (size[0] - line_width) / 3
font_size = int(block_size * 0.7)

class BoardView:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    size = (500, 500)
    line_width = 4
    block_size = (size[0] - line_width) / 3
    font_size = int(block_size * 0.7)

    def __init__(self, board):
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.board = board
        self.done = False
        self.font = pygame.font.SysFont('Calibri', self.font_size, True, False)
        self.init_board()

    def init_board(self):
        self.draw_blank()


    def draw_blank(self):
        self.screen.fill(self.WHITE)
        coord_1 = self.block_size + self.line_width / 2
        coord_2 = self.block_size * 2 + self.line_width / 2 + self.line_width
        pygame.draw.line(self.screen, self.BLACK, [coord_1, 0], [coord_1, self.size[0]], self.line_width)
        pygame.draw.line(self.screen, self.BLACK, [coord_2, 0], [coord_2, self.size[0]], self.line_width)
        pygame.draw.line(self.screen, self.BLACK, [0, coord_1], [self.size[0], coord_1], self.line_width)
        pygame.draw.line(self.screen, self.BLACK, [0, coord_2], [self.size[0], coord_2], self.line_width)
        pygame.display.flip()

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                mark = self.board.get(i, j)
                if mark != 0:
                    x = j * self.block_size + self.block_size / 2 + j * self.line_width - self.block_size / 4
                    y = i * self.block_size + self.block_size / 2 + i * self.line_width - self.block_size / 4
                    mark_value = 'X' if mark == 1 else 'O'
                    text = self.font.render(mark_value, True, self.BLACK)
                    self.screen.blit(text, [x, y])
        pygame.display.flip()

    def update(self):
        self.draw_board()

    def reset(self):
        self.draw_blank()
