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

    def test_is_choice_valid_returns_false_for_invalid_choice(self):
        game = TicTacToe()
        game.set_board_size(3)
        game.set_player_one("John")
        game.set_player_two("Jack")
        self.assertFalse(game.is_choice_valid('ABC'))

    def test_is_choice_available_returns_false_for_already_taken_choice(self):
        game = TicTacToe()
        game.set_board_size(3)
        game.set_player_one("John")
        game.set_player_two("Jack")
        game.first_choice_player("1")
        game.mark_choice("1")
        self.assertFalse(game.is_choice_available("1"))

    def test_make_choice_changes_the_player_turn_after_choice(self):
        game = TicTacToe()
        game.set_board_size(3)
        game.set_player_one("John")
        game.set_player_two("Jack")
        game.first_choice_player("1")
        game.mark_choice("1")
        self.assertEqual(game.get_player_two(), game.get_turn())
        self.assertEqual(game.get_game_board()['1'], 'X')

    def test_get_available_choices_returns_list_of_available_choices(self):
        game = TicTacToe()
        game.set_board_size(3)
        game.set_player_one("John")
        game.set_player_two("Jack")
        game.first_choice_player("1")
        game.mark_choice("1")
        self.assertEqual(game.get_available_choices(), [
                         '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_mark_choice_changes_the_board_after_choice(self):
        game = TicTacToe()
        game.set_board_size(3)
        game.set_player_one("John")
        game.set_player_two("Jack")
        game.first_choice_player("1")
        game.mark_choice("1")
        self.assertEqual(game.get_game_board(), {
            '1': 'X', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '})

    def test_get_winner(self):
        game = TicTacToe()
        game.set_board_size(3)
        game.set_player_one("John")
        game.set_player_two("Jack")
        game.first_choice_player("1")
        game._TicTacToe__game_board = {
            '1': 'X', '2': 'X', '3': 'X', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
        self.assertEqual(game.get_winner(), (True, game.get_player_one()))

    def test_get_winning_combinations(self):
        game = TicTacToe()
        game.set_board_size(3)
        self.assertEqual(game.get_winning_combinations(), [
                         ('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), ('1', '4', '7'), (
                             '2', '5', '8'), ('3', '6', '9'), ('1', '5', '9'), ('3', '5', '7')])

    def test_get_available_combinations(self):
        game = TicTacToe()
        game.set_board_size(3)
        game._TicTacToe__game_board = {
            '1': 'X', '2': 'X', '3': 'O', '4': 'X', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
        self.assertEqual(game.get_available_combinations(), [('4', '5', '6'), ('7', '8', '9'), ('1', '4', '7'), (
            '2', '5', '8'), ('3', '6', '9'), ('1', '5', '9'), ('3', '5', '7')])

    def test_get_combination_weight(self):
        game = TicTacToe()
        game.set_board_size(3)
        game._TicTacToe__game_board = {
            '1': 'X',
            '2': 'X',
            '3': 'O',
            '4': 'X',
            '5': ' ',
            '6': ' ',
            '7': ' ',
            '8': ' ',
            '9': 'O'
        }
        self.assertEqual(game.get_combination_weight(('1', '2', '3'), 'X'), 1)
        self.assertEqual(game.get_combination_weight(('4', '5', '6'), 'X'), 0)
        self.assertEqual(game.get_combination_weight(('3', '6', '9'), 'X'), -1)

    def test_get_computer_choice(self):
        game = TicTacToe()
        game.set_board_size(3)
        game.set_player_one("John")
        game.set_player_two("COMP")
        game.first_choice_player("1")
        game._TicTacToe__game_board = {
            '1': 'X', '2': 'X', '3': ' ', '4': 'X', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
        self.assertEqual(game.get_computer_choice(), '3')
        game._TicTacToe__game_board = {
            '1': 'X', '2': 'X', '3': 'O', '4': 'X', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
        self.assertEqual(game.get_computer_choice(), '7')


if __name__ == '__main__':
    unittest.main()
