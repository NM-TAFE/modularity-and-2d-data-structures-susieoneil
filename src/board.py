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
        """
        Initializes a new instance of the Board class.

        Args:
            size (int, optional): The size of the board. Defaults to 3.
        """
        self.size = size
        self.grid = self._create_2d_grid()

    def _create_2d_grid(self):
        """
        Creates a 2-dimensional square grid of the board.

        Returns:
            list: Square 2d list of None values
        """
        row = [None] * self.size
        return [row.copy() for _ in range(self.size)]

    def is_full(self) -> bool:
        """
        Checks if the all positions on the board are filled.

        Returns:
            bool: False if any None values, True otherwise
        """
        for row in self.grid:
            if None in row:
                return False
        return True

    def is_position_occupied(self, row, col) -> bool:
        """
        Checks if board position already has a player

        Args:
            row (int): the index of a row in the grid
            col (int): the index of an item in the row

        Returns:
            bool: False if no player, True otherwise
        """
        return self.grid[row][col] is not None

    def make_move(self, row, col, player) -> None:
        """
        Checks a move is valid and adds player to board position

        Args:
            row (int): index of the row
            col (int): index of the column
            player (Player): the current player
        """
        if row not in range(0, self.size) or col not in range(0, self.size):
            raise InvalidPositionError("Invalid position")
        if self.is_position_occupied(row, col):
            raise PositionOccupiedError("Position already occupied")

        self.grid[row][col] = player

    def get_winner(self) -> None | Player:
        """
        Checks if the board contains a winning player.

        Returns:
             None or Player: Winner if any, None otherwise.
        """
        return self._has_horizontal_winner() or self._has_vertical_winner() or self._has_diagonal_winner()

    def _has_horizontal_winner(self) -> None | Player:
        """
        Checks each row in the board for a winning player.

        Returns:
             None or Player: Winner if any, None otherwise.
        """
        for row in self.grid:
            player = row[0]
            if player and all(players == player for players in row):
                return player

    def _has_vertical_winner(self) -> None | Player:
        """
        Checks each column in the grid for a winning player.

        Returns:
             None or Player: Winner if any, None otherwise.
        """
        for col, player in enumerate(self.grid[0]):
            if not player:
                continue
            column = []
            for row in self.grid:
                column.append(row[col])
            if all(players == player for players in column):
                return player

    def _has_diagonal_winner(self) -> None | Player:
        """
        Checks the right and left diagonals in the grid for a winning player.

        Returns:
             None or Player: Winner if any, None otherwise.
        """
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
        """
        Returns a string representation of the board.

        Returns:
            str: The string representation of the board.
        """
        board_string = ""
        row_divider = "---"
        col_divider = "|"
        for i, row in enumerate(self.grid):
            # generate a string for each row
            for j, col in enumerate(row):
                board_string += (f" {str(col)} " if col else "   ")
                board_string += col_divider if j != (self.size - 1) else "\n"
            # generate a divider after each row except the last
            if i != (self.size - 1):
                board_string += row_divider + ((col_divider + row_divider) * (self.size - 1)) + "\n"
        return board_string
