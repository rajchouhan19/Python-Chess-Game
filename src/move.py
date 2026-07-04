class Move:

    def __init__(self, row, col, capture=False):

        self.row = row
        self.col = col
        self.capture = capture

    def position(self):
        return (self.row, self.col)


class HistoryMove:

    def __init__(
        self,
        start_row,
        start_col,
        end_row,
        end_col,
        piece,
        captured_piece=None,
    ):

        self.start_row = start_row
        self.start_col = start_col

        self.end_row = end_row
        self.end_col = end_col

        self.piece = piece
        self.captured_piece = captured_piece