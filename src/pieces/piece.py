import pygame
from ..constants import SQUARE_SIZE
from ..move import Move

class Piece:

    SYMBOLS = {
        "pawn": "P",
        "rook": "R",
        "knight": "N",
        "bishop": "B",
        "queen": "Q",
        "king": "K",
    }

    def __init__(self, color, piece_type):

        self.color = color
        self.type = piece_type
        self.has_moved = False

        filename = (
            f"assets/pieces/"
            f"{color[0]}{self.SYMBOLS[piece_type]}.png"
        )

        self.image = pygame.image.load(filename).convert_alpha()

        self.image = pygame.transform.smoothscale(
            self.image,
            (SQUARE_SIZE - 8, SQUARE_SIZE - 8),
        )

    def get_valid_moves(self, board, row, col):
        return []

    def get_sliding_moves(self, board, row, col, directions):

        moves = []

        for dr, dc in directions:

            r = row + dr
            c = col + dc

            while 0 <= r < 8 and 0 <= c < 8:

                piece = board.get_piece(r, c)

                if piece is None:

                    moves.append(
                    Move(
                        r,
                        c
                    )
                )

                elif piece.color != self.color:

                    moves.append(
                        Move(
                            r,
                            c,
                            True
                        )
                    )

                    break

                else:
                    break

                r += dr
                c += dc

        return moves