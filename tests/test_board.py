import unittest
from src.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()  # The default 3x3 grid to use for non-custom boards

    def test_create_2d_grid_with_size_2_makes_a_2x2_2d_list_of_none_values(self):
        size = 2
        self.assertListEqual(Board(size)._create_2d_grid(),
                             [[None, None],
                              [None, None]])

    def test_create_2d_grid_without_size_makes_a_3x3_2d_list_of_none_values(self):
        self.assertListEqual(self.board._create_2d_grid(),
                             [[None, None, None],
                              [None, None, None],
                              [None, None, None]])

    def test_create_2d_grid_rows_are_unique_lists(self):
        self.assertIsNot(self.board.grid[1], self.board.grid[2])

    def test_is_full_returns_false_if_grid_contains_none(self):
        self.assertEqual(self.board.is_full(), False)

    def test_has_horizontal_winner_returns_valid_player_from_row_where_all_same(self):
        player = 'x'
        board = Board(3)
        board.grid = [[None, None, None],
                      ['x', 'o', 'o'],
                      ['x', 'x', 'x']]

        self.assertIsNot(board._has_horizontal_winner(), None)
        self.assertIs(board._has_horizontal_winner(), player)

    def test_has_vertical_winner_returns_valid_player_from_column_where_all_same(self):
        board = Board(3)
        board.grid = [['x', None, 'o'],
                      ['x', None, 'o'],
                      [None, None, 'o']]

        self.assertIsNot(board._has_vertical_winner(), 'x')
        self.assertIsNot(board._has_vertical_winner(), None)
        self.assertIs(board._has_vertical_winner(), 'o')

    def test_has_diagonal_winner_returns_valid_player_from_diagonal_where_all_same(self):
        board_empty = Board()
        board_right = Board(3)
        board_left = Board(3)

        board_right.grid = [['x', 'o', None],
                            ['x', 'x', 'o'],
                            ['o', 'o', 'x']]

        board_left.grid = [[None, 'x', 'o'],
                           ['x', 'o', 'x'],
                           ['o', 'x', 'x']]

        self.assertIsNone(board_empty._has_diagonal_winner())
        self.assertIs(board_right._has_diagonal_winner(), 'x')
        self.assertIs(board_left._has_diagonal_winner(), 'o')

    def test_string_override_returns_a_suitable_game_grid(self):
        self.assertEqual(str(self.board), "\n"
                                          "   |   |   \n"
                                          "---|---|---\n"
                                          "   |   |   \n"
                                          "---|---|---\n"
                                          "   |   |   \n")
