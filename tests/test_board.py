import unittest
from src.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()   # The default 3x3 grid to use for most tests

    def test_create_2d_grid_with_size_2_makes_a_2x2_2d_list_of_None_values(self):
        size = 2
        self.assertListEqual(Board(size)._create_2d_grid(),
                             [[None, None],
                              [None, None]])

    def test_create_2d_grid_without_size_makes_a_3x3_2d_list_of_None_values(self):
        self.assertListEqual(self.board._create_2d_grid(),
                             [[None, None, None],
                              [None, None, None],
                              [None, None, None]])

    def test_is_full_returns_false_if_grid_contains_none(self):
        self.assertEqual(self.board.is_full(), False)
