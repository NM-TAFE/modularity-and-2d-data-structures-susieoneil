import unittest
from src.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()  # The default 3x3 grid to use for non-custom boards

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

    def test_create_2d_grid_rows_are_unique_lists(self):
        self.assertIsNot(self.board.grid[1], self.board.grid[2])

    def test_is_full_returns_false_if_grid_contains_none(self):
        self.assertEqual(self.board.is_full(), False)

    def test_has_horizontal_winner_returns_valid_player_from_row_where_all_same(self):
        # Set up a board with a winner 'x' on row 1
        board = Board()
        empty_row = 0
        win_row = 1
        player = 'x'
        for col in range(board.size):
            board.grid[win_row][col] = player
        # Check board was created
        self.assertIn(None, board.grid[empty_row])
        self.assertIn(player, board.grid[win_row])

        self.assertIsNot(board._has_horizontal_winner(), None)
        self.assertIs(board._has_horizontal_winner(), player)
