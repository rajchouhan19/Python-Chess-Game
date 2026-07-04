from .piece import Piece
from ..move import Move

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color, "pawn")

    def get_valid_moves(self, board, row, col):

        moves = []

        direction = -1 if self.color == "white" else 1

        # Forward
        if board.get_piece(row + direction, col) is None:

            moves.append(
                Move(
                    row + direction,
                    col
                )
            )

            if not self.has_moved:

                if board.get_piece(row + 2 * direction, col) is None:

                    moves.append(
                        Move(
                            row + 2 * direction,
                            col
                        )
                    )

        # Left Capture

        left = board.get_piece(row + direction, col - 1)

        if left and left.color != self.color:

            moves.append(
                Move(
                    row + direction,
                    col - 1,
                    True
                )
            )

        # Right Capture

        right = board.get_piece(row + direction, col + 1)

        if right and right.color != self.color:

            moves.append(
                Move(
                    row + direction,
                    col + 1,
                    True
                )
            )

        return moves