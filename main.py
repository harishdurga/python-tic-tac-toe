from classes import TicTacToe
import os


def main():
    game = TicTacToe()
    is_game_won = False
    winner = ''

    print("Welcome To Tic Tac Toe")

    # Reading board size
    while True:
        try:
            game.set_board_size(int((input(
                'Enter the size for Tic Tac Toe board:')).strip()))
            break
        except ValueError as e:
            print(
                "Invalid size. Please enter valid intenger for board size. Minimum size is 3")

    game.show_instructions()

    # Read player 1 name
    while True:
        try:
            game.set_player_one((input(
                'Enter the name for first player(X):')).strip())
        except Exception as e:
            print(e)
            continue
        break

    # Reading player two name
    while True:
        try:
            game.set_player_two(input(
                'Enter name for second player(O):').strip())
        except Exception as e:
            print(e)
            continue
        break

    # Setting the player to make the first choice or move
    while True:
        try:
            game.first_choice_player(input(
                "Enter 1 for player one to make the first move, 2 for the second player.:").strip())
            break
        except ValueError:
            print("Invalid player.")
            continue

    game.draw_board()

    for i in range(game.get_board_size()*game.get_board_size()):
        while True:
            if game.get_turn() == 'COMP':
                choice = game.get_computer_choice()
                break
            choice = input("Please enter {}'s({}) choice from ({}):".format(
                game.get_turn(), ('X' if game.get_turn() == game.get_player_one() else 'O'), ",".join(game.get_available_choices()))).strip()
            if game.is_choice_valid(choice):
                if game.is_choice_available(choice):
                    break
                else:
                    print("Choice {} is not available. Choose any number from ({}).".format(
                        choice, ",".join(game.get_available_choices())))
            else:
                print(
                    "Choice {} is not valid. Please select any number from Choose any number from ({}).".format(choice, ",".join(game.get_available_choices())))
        game.mark_choice(choice)
        os.system('cls' if os.name == 'nt' else 'clear')
        game.draw_board()
        is_game_won, winner = game.get_winner()
        if is_game_won:
            os.system('cls' if os.name == 'nt' else 'clear')
            game.draw_board()
            print("player {} won!!!!".format(winner))
            break

    if is_game_won == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        game.draw_board()
        print("It's a draw!!!")


if __name__ == '__main__':
    while True:
        main()
        input(
            "Would you like to play again? if yes press enter otherwise exit the program.")
