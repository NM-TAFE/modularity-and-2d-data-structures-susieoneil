class Player:
    def __init__(self, symbol):
        """
        Initializes a new instance of the Player class.

        Args:
            symbol (str): An Ascii character used to represent the player.
            # ... Should be constrained to a single character.
        """
        self.symbol = symbol

    def __str__(self) -> str:
        """
        Returns a string representation of the player.

        Returns:
            str: The string representation of the player.
        """
        return self.symbol
