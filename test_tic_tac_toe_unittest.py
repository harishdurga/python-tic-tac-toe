import unittest
from classes import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_empty_name_is_not_allowed_for_players(self):
        game = TicTacToe()
        self.assertRaises(
            Exception, game.set_player_one, "\n")
        self.assertRaises(
            Exception, game.set_player_two, " ")
        self.assertRaises(
            Exception, game.set_player_two, "")

    def test_same_name_is_not_allowed_for_players(self):
        game = TicTacToe()
        game.set_player_one("John")
        self.assertRaises(
            Exception, game.set_player_two, "John")


if __name__ == '__main__':
    unittest.main()
