from .piece import Piece

class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color, "bishop")

    def get_valid_moves(self, board, row, col):

        directions = [

            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),

        ]

        return self.get_sliding_moves(
            board,
            row,
            col,
            directions,
        )