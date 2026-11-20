import unittest

from gui_tic_tac_toe import TicTacToeModel


class TicTacToeModelTests(unittest.TestCase):
    def test_player_x_wins_row(self):
        model = TicTacToeModel()
        for position in (0, 3, 1, 4, 2):
            self.assertTrue(model.play(position))

        self.assertEqual(model.winner, "X")
        self.assertEqual(model.winning_line, (0, 1, 2))
        self.assertTrue(model.is_over)

    def test_player_o_wins_column(self):
        model = TicTacToeModel()
        for position in (0, 1, 3, 4, 8, 7):
            self.assertTrue(model.play(position))

        self.assertEqual(model.winner, "O")
        self.assertEqual(model.winning_line, (1, 4, 7))

    def test_occupied_square_is_rejected(self):
        model = TicTacToeModel()
        self.assertTrue(model.play(4))
        self.assertFalse(model.play(4))
        self.assertEqual(model.move_count, 1)
        self.assertEqual(model.current_player, "O")

    def test_draw_is_detected(self):
        model = TicTacToeModel()
        for position in (0, 1, 2, 4, 3, 5, 7, 6, 8):
            self.assertTrue(model.play(position))

        self.assertTrue(model.is_draw)
        self.assertIsNone(model.winner)

    def test_reset_clears_game_state(self):
        model = TicTacToeModel()
        model.play(0)
        model.play(4)
        model.reset()

        self.assertEqual(model.board, [""] * 9)
        self.assertEqual(model.current_player, "X")
        self.assertEqual(model.move_count, 0)
        self.assertIsNone(model.winner)


if __name__ == "__main__":
    unittest.main()
