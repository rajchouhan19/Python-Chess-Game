from ..move import Move
from .piece import Piece


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color, "knight")

    def get_valid_moves(self, board, row, col):

        moves = []

        offsets = [

            (-2, -1),
            (-2, 1),

            (-1, -2),
            (-1, 2),

            (1, -2),
            (1, 2),

            (2, -1),
            (2, 1),

        ]

        for dr, dc in offsets:

            r = row + dr
            c = col + dc
            if not (0 <= r < 8 and 0 <= c < 8):
                continue
            piece = board.get_piece(r, c)

            # Empty square
            if piece is None:

                moves.append(
                    Move(
                        r,
                        c,
                    )
                )


            # Enemy piece
            elif piece.color != self.color:

                moves.append(
                    Move(
                        r,
                        c,
                        True
                    )
                )

        return moves