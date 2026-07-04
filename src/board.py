import pygame
from .move import Move, HistoryMove

from .constants import *
# from .piece import Piece
from .pieces.pawn import Pawn
from .pieces.rook import Rook
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .pieces.queen import Queen
from .pieces.king import King

class Board:

    def __init__(self):

        self.grid = [[None for _ in range(8)] for _ in range(8)]

        self.setup_board()
        self.move_history = []
        self.light_color = CLASSIC_LIGHT
        self.dark_color = CLASSIC_DARK
    def setup_board(self):

        back_row = [
            Rook,
            Knight,
            Bishop,
            Queen,
            King,
            Bishop,
            Knight,
            Rook,
        ]

        for col, piece_class in enumerate(back_row):

            self.grid[0][col] = piece_class("black")
            self.grid[1][col] = Pawn("black")

            self.grid[6][col] = Pawn("white")
            self.grid[7][col] = piece_class("white")
    def set_theme(self, theme):

        if theme == "classic":

            self.light_color = CLASSIC_LIGHT
            self.dark_color = CLASSIC_DARK

        elif theme == "dark":

            # Feel free to tweak these colors
            self.light_color = (80, 80, 90)
            self.dark_color = (35, 35, 45)

    def draw(self, screen, selected=None, valid_moves=None):

        if valid_moves is None:
            valid_moves = []

        light = self.light_color
        dark = self.dark_color      

        for row in range(ROWS):
            for col in range(COLS):

                color = light if (row + col) % 2 == 0 else dark

                pygame.draw.rect(
                    screen,
                    color,
                    (
                        col * SQUARE_SIZE,
                        row * SQUARE_SIZE,
                        SQUARE_SIZE,
                        SQUARE_SIZE,
                    ),
                )

                if selected == (row, col):

                    pygame.draw.rect(
                        screen,
                        SELECTED,
                        (
                            col * SQUARE_SIZE,
                            row * SQUARE_SIZE,
                            SQUARE_SIZE,
                            SQUARE_SIZE,
                        ),
                        width=4,
                    )
                # draw legal move dots

                for move in valid_moves:

                    if move.row == row and move.col == col: 

                        if move.capture:

                            pygame.draw.circle(
                                screen,
                                (220, 60, 60),
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                                ),
                                26,
                                3,
                            )

                        else:

                            pygame.draw.circle(
                                screen,
                                (60, 180, 75),
                                (
                                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                                ),
                                10,
                            )

                piece = self.grid[row][col]

                if piece:

                    screen.blit(
                        piece.image,
                        (
                            col * SQUARE_SIZE + 4,
                            row * SQUARE_SIZE + 4,
                        ),
                    )

    def get_piece(self, row, col):

        if 0 <= row < 8 and 0 <= col < 8:
            return self.grid[row][col]

        return None

    def move_piece(self, start, end):

        sr, sc = start
        er, ec = end

        piece = self.grid[sr][sc]
        captured_piece = self.grid[er][ec]

        move = HistoryMove(
            sr,
            sc,
            er,
            ec,
            piece,
            captured_piece
        )

        self.move_history.append(move)

        self.grid[er][ec] = piece
        self.grid[sr][sc] = None
        print(
            f"{self.to_notation(sr,sc)} -> "
            f"{self.to_notation(er,ec)}"
        )
        piece.has_moved = True
    FILES = "abcdefgh"

    def to_notation(self, row, col):

        file = self.FILES[col]
        rank = str(8 - row)

        return file + rank
    def get_all_moves(self, color):

        all_moves = []

        for row in range(8):

            for col in range(8):

                piece = self.get_piece(row, col)

                if piece is None:
                    continue

                if piece.color != color:
                    continue

                valid_moves = piece.get_valid_moves(
                    self,
                    row,
                    col
                )

                for move in valid_moves:

                    all_moves.append(
                        (
                            (row, col),
                            move
                        )
                    )

        return all_moves