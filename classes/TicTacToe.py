from interfaces import TicTacToeInterface
import os


class TicTacToe(TicTacToeInterface):
    def __init__(self) -> None:
        self.__player_one = ''
        self.__player_two = ''
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
        self.__is_game_won = False
        self.__winner = ''

    def __welcome(self):
        print("Welcome to Tic Tac Toe")
        print('7' + '|' + '8' + '|' + '9')
        print('-+-+-')
        print('4' + '|' + '5' + '|' + '6')
        print('-+-+-')
        print('1' + '|' + '2' + '|' + '3')
        print("Instructions:")
        print("- To play with computer please enter COMP as second player")
        print("- To make your move, select any of the available number(1-9)")

    def __get_players(self):
        try:
            while self.__player_one == '':
                self.__player_one = input(
                    'Enter the name for first player(X):')
            while self.__player_two == '' or self.__player_two == self.__player_one:
                if self.__player_two == self.__player_one:
                    print("Please enter a different name for second player(O)")
                self.__player_two = input(
                    "Enter the name for second player(O):")
        except Exception as e:
            print(e)

    def __draw_board(self):
        print(('7' if self.__game_board['7'] == ' ' else self.__game_board['7'])
              + '|'
              + ('8' if self.__game_board['8'] ==
                 ' ' else self.__game_board['8'])
              + '|'
              + ('9' if self.__game_board['9'] ==
                 ' ' else self.__game_board['9'])
              )
        print('-+-+-')
        print(('4' if self.__game_board['4'] == ' ' else self.__game_board['4'])
              + '|'
              + ('5' if self.__game_board['5'] ==
                 ' ' else self.__game_board['5'])
              + '|'
              + ('6' if self.__game_board['6'] ==
                 ' ' else self.__game_board['6'])
              )
        print('-+-+-')
        print(('1' if self.__game_board['1'] == ' ' else self.__game_board['1'])
              + '|'
              + ('2' if self.__game_board['2'] ==
                 ' ' else self.__game_board['2'])
              + '|'
              + ('3' if self.__game_board['3'] ==
                 ' ' else self.__game_board['3'])
              )

    def __get_available_choices(self) -> list:
        valid_choices = []
        for key in self.__game_board:
            if self.__game_board[key] == ' ':
                valid_choices.append(key)
        return valid_choices

    def __is_choice_available(self, choice: str) -> bool:
        if self.__game_board[choice] != ' ':
            return False
        else:
            return True

    def __is_choice_valid(self, choice: str) -> bool:
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        else:
            return False

    def __get_winner(self) -> "tuple[bool, str]":
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

    def start_game(self):
        self.__welcome()
        self.__get_players()
        self.__turn = self.__player_one
        for i in range(9):
            self.__draw_board()

            while True:
                choice = input("Please enter {}'s({}) choice from ({}):".format(
                    self.__turn, ('X' if self.__turn == self.__player_one else 'O'), ",".join(self.__get_available_choices())))
                if self.__is_choice_valid(choice):
                    if self.__is_choice_available(choice):
                        break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Choice {} is not available. Choose any number from ({}).".format(
                            choice, ",".join(self.__get_available_choices())))
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(
                        "Choice {} is not valid. Please select any number from Choose any number from ({}).".format(choice, ",".join(self.__get_available_choices())))
            self.__game_board[choice] = 'X' if self.__turn == self.__player_one else 'O'
            self.__turn = self.__player_two if self.__turn == self.__player_one else self.__player_one
            self.__is_game_won, self.__winner = self.__get_winner()
            if self.__is_game_won:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.__draw_board()
                print("player {} won!!!!".format(self.__winner))
                break
            os.system('cls' if os.name == 'nt' else 'clear')
        if self.__is_game_won == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.__draw_board()
            print("It's a draw!!!")
