from .piece import Piece

class Rook(Piece):

    def __init__(self, color):
        super().__init__(color, "rook")

    def get_valid_moves(self, board, row, col):

        directions = [

            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),

        ]

        return self.get_sliding_moves(
            board,
            row,
            col,
            directions,
        )