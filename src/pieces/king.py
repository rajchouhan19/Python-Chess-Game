from .piece import Piece
from ..move import Move

class King(Piece):

    def __init__(self, color):
        super().__init__(color, "king")

    def get_valid_moves(self, board, row, col):

        moves = []

        offsets = [

            (-1, -1),
            (-1, 0),
            (-1, 1),

            (0, -1),
            (0, 1),

            (1, -1),
            (1, 0),
            (1, 1),

        ]

        for dr, dc in offsets:

            r = row + dr
            c = col + dc
            if not (0 <= r < 8 and 0 <= c < 8):
                continue
            piece = board.get_piece(r, c)

            if piece is None:

                moves.append(
                    Move(
                        r,
                        c,
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

        return moves