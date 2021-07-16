from interfaces import TicTacToeInterface
import math


class TicTacToe(TicTacToeInterface):
    def __init__(self) -> None:
        self.__player_one = None
        self.__player_two = None
        self.__turn = ''
        self.__game_board = {
            '1': ' ',
            '2': ' ',
            '3': ' ',
            '4': ' ',
            '5': ' ',
            '6': ' ',
            '7': ' ',
            '8': ' ',
            '9': ' '
        }
        self.__board_size = 3

    def show_instructions(self):
        self.draw_board()
        print("Instructions:")
        print("- To play with computer please enter COMP as second player")
        print("- To make your move, select any of the available number(1-9)")

    def set_player_one(self, name: str):
        if name == "" or name == " " or name == "\n":
            raise Exception("Player one name cannot be empty")
        if name == self.__player_two:
            raise Exception("Player one name cannot be same as player two")
        self.__player_one = name

    def set_player_two(self, name: str):
        if name == "" or name == " " or name == "\n":
            raise Exception("Player one name cannot be empty")
        if name == self.__player_one:
            raise Exception("Player two name cannot be same as player one")
        self.__player_two = name

    def first_choice_player(self, player: str):
        if player != "1" and player != "2":
            raise ValueError
        self.__turn = self.__player_one if player == "1" else self.__player_two

    def get_turn(self) -> str:
        return self.__turn

    def get_player_one(self) -> str:
        return self.__player_one

    def get_player_two(self) -> str:
        return self.__player_two

    def draw_board(self):
        j = 1
        n = self.__board_size
        for i in range(n):
            str_one = ""
            str_two = ""
            while j <= n*(i+1):
                cell_value = str(j) if self.__game_board[str(
                    j)] == ' ' else self.__game_board[str(j)]
                if j != n*(i+1):
                    str_one += " "+cell_value+"|" if j <= 9 else cell_value+"|"
                    str_two += "--+" if j > 9 else "--+"
                else:
                    str_one += " "+cell_value if j <= 9 else cell_value
                    str_two += "--"
                j = j+1
            print(str_one)
            if (i+1) != n:
                print(str_two)

    def get_available_choices(self) -> list:
        valid_choices = []
        for key in self.__game_board:
            if self.__game_board[key] == ' ':
                valid_choices.append(key)
        return valid_choices

    def is_choice_available(self, choice: str) -> bool:
        if self.__game_board[choice] != ' ':
            return False
        else:
            return True

    def is_choice_valid(self, choice: str) -> bool:
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        else:
            return False

    def mark_choice(self, choice):
        self.__game_board[choice] = 'X' if self.__turn == self.__player_one else 'O'
        self.__turn = self.__player_two if self.__turn == self.__player_one else self.__player_one

    def get_winner(self) -> "tuple[bool, str]":
        winning_combinations = [
            ('1', '2', '3'),
            ('4', '5', '6'),
            ('7', '8', '9'),
            ('1', '4', '7'),
            ('2', '5', '8'),
            ('3', '6', '9'),
            ('1', '5', '9'),
            ('3', '5', '7')
        ]
        for combination in winning_combinations:
            if self.__game_board[combination[0]] != ' ' and self.__game_board[combination[1]] != ' ' and self.__game_board[combination[2]] != ' ' and (self.__game_board[combination[0]] == self.__game_board[combination[1]] == self.__game_board[combination[2]]):
                return True, (self.__player_one if self.__game_board[combination[0]] == 'X' else self.__player_two)
        return False, ''

    def set_board_size(self, size: int):
        if size < 3:
            raise ValueError
        self.__game_board = {}
        self.__board_size = size
        for i in range(size*size):
            self.__game_board[str(i+1)] = ' '
