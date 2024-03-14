from player import Player


class BoardError(Exception):
    """Base class for all board errors
    """


class InvalidPositionError(BoardError):
    """Called when a position requested is out of bounds
    """


class PositionOccupiedError(BoardError):
    """Called when a position requested is already occupied
    """


class Board:
    def __init__(self, size=3) -> None:
        self.size = size
        self.grid = self._create_2d_grid()

    def _create_2d_grid(self):
        row = [None] * self.size
        return [row.copy() for _ in range(self.size)]

    def is_full(self) -> bool:
        for row in self.grid:
            if None in row:
                return False
        return True

    def is_position_occupied(self, row, col) -> bool:
        return self.grid[row][col] is not None

    def make_move(self, row, col, player) -> None:
        # Fixed the logic not raising the error (see source: Check Range Separately)
        # if row < 0 or row >= self.size or col < 0 or col >= self.size:
        # Using range() might improve readability.
        if row not in range(0, self.size) or col not in range(0, self.size):
            raise InvalidPositionError("Invalid position")
        if self.is_position_occupied(row, col):
            raise PositionOccupiedError("Position already occupied")

        self.grid[row][col] = player

    def get_winner(self) -> None | Player:
        return self._has_horizontal_winner() or self._has_vertical_winner() or self._has_diagonal_winner()

    def _has_horizontal_winner(self) -> None | Player:
        for row in self.grid:
            player = row[0]
            if player and all(players == player for players in row):
                return player

    def _has_vertical_winner(self) -> None | Player:
        for col, player in enumerate(self.grid[0]):
            if not player:
                continue
            column = []
            for row in self.grid:
                column.append(row[col])
            if all(players == player for players in column):
                return player

    def _has_diagonal_winner(self) -> None | Player:
        # check player in right diagonal
        player_right = self.grid[0][0]
        if player_right:
            col = 0
            diagonal_right = []
            for row in self.grid:
                diagonal_right.append(row[col])
                col += 1
            if all(players == player_right for players in diagonal_right):
                return player_right

        # check player in left diagonal
        player_left = self.grid[0][-1]
        if player_left:
            col = -1
            diagonal_left = []
            for row in self.grid:
                diagonal_left.append(row[col])
                col -= 1
            if all(players == player_left for players in diagonal_left):
                return player_left

    def __str__(self) -> str:
        return "\n".join([str([str(col) if col else ' ' for col in row])
                          for row in self.grid])


if __name__ == '__main__':
    pass
