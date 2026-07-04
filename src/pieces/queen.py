from .piece import Piece
class Queen(Piece):

    def __init__(self, color):
        super().__init__(color, "queen")

    def get_valid_moves(self, board, row, col):

        directions = [

            # Bishop

            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),

            # Rook

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