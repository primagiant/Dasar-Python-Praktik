import pygame
import sys
import numpy as np

from pygame.constants import QUIT

pygame.init()
SIZE = WIDTH, HEIGHT = 600, 600
DISPLAY = pygame.display.set_mode(SIZE)

# Title
pygame.display.set_caption("Game Derek")

# Color
RED = (255, 80, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (80, 80, 255)
ORANGE = (255, 180, 80)
LINE_COLOR = (255, 160, 80)

# Bacground Color
DISPLAY.fill(ORANGE)

# Ukuran
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3

# Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def drawLine():
    pygame.draw.line(DISPLAY, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(DISPLAY, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(DISPLAY, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(DISPLAY, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def markLocation(row, col, player):
    board[row][col] == player


def isLocationEmpty(row, col):
    return board[row][col] == 0


def isBoardFull():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


    # Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clikedRow = int(mouseY // 200)
            clikedCol = int(mouseX // 200)

            print(clikedRow)
            print(clikedCol)

    drawLine()
    pygame.display.update()
