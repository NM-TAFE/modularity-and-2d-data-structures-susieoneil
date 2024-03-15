from player import Player
from board import Board, BoardError


class Game:
    """
    Represents a Tic-Tac-Toe game.

    Attributes:
        board (Board): The game board.
        players (list[Player]): The list of players.
        current_player (Player): The current player.
    """

    def __init__(self, size=3) -> None:
        """
        Initializes a new instance of the Game class.

        Args:
            size (int, optional): The size of the game board. Defaults to 3.
        """
        self.board = Board(size)
        self.players = [Player("X"), Player("O")]
        self.current_player = self.players[0]

    def play(self) -> None:
        """
        Starts the game and allows players to make moves until the game is over.
        Prints the game board after each move.
        Prints the winner or a draw message at the end of the game.
        """
        while not self.is_over():
            print(self)
            print(f"Player {self.current_player.symbol} enter row (0-2): ", end='')
            row = self.get_int_from_input()
            print(f"Player {self.current_player.symbol} enter col (0-2): ", end='')
            col = self.get_int_from_input()

            self.make_move(row, col)

        print(self)
        winner = self.get_winner()
        if winner is None:
            print("It's a draw!")
        else:
            print(f"Player {winner.symbol} wins!")

    @staticmethod
    def get_int_from_input() -> int:
        """
        Takes and validates user input until an integer is entered.

        Returns:
             value: an integer
        """
        input_value = ''
        while not input_value.isdigit():
            input_value = input()
            try:
                value = int(input_value)
            except ValueError:
                print("Invalid input, enter a number: ", end='')
                continue
            else:
                return value

    def make_move(self, row, col) -> None:
        """
        Makes a move on the game board at the specified row and column.
        If the move is invalid, prints an error message.

        Args:
            row (int): The row index.
            col (int): The column index.
        """
        try:
            self.board.make_move(row, col, self.current_player)
        except BoardError as e:
            print(e)
        else:
            self.current_player = self.players[0] if self.current_player is self.players[1] else self.players[1]

    def is_over(self) -> bool:
        """
        Checks if the game is over.
        The game is over if there is a winner or the board is full.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.board.get_winner() is not None or self.board.is_full()

    def __str__(self) -> str:
        """
        Returns a string representation of the game board.

        Returns:
            str: The string representation of the game board.
        """
        return str(self.board)

    def get_winner(self) -> None | Player:
        """
        Gets the winner of the game, if any.

        Returns:
            None or Player: The winner of the game, or None if there is no winner yet.
        """
        return self.board.get_winner()

    def get_current_player(self) -> Player:
        """
        Gets the current player.

        Returns:
            Player: The current player.
        """
        return self.current_player


def play_tic_tac_toe():
    """
    Start and play a game
    """
    game = Game()
    game.play()


if __name__ == '__main__':
    play_tic_tac_toe()
