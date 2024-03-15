import unittest
from src.game import Game


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()
