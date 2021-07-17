class TicTacToeInterface:

    def set_board_size(self, size: int):
        """This will set the size of the tic tac toe board. if size is 4 then the board size will 4*4 totaling to 16 cells"""
        pass

    def set_player_one(self, name: str):
        """Set the name of the player one. Cannot be same name as the second player"""
        pass

    def set_player_two(self, name: str):
        """Set the name of the second player. Cannot be same name as the first player"""
        pass

    def show_instructions():
        """Print out the game instructions to terminal"""
        pass

    def first_choice_player(self, player: str):
        """Set which player to make the first move/choice. 1 to select first player and 2 for the second player"""
        pass

    def get_turn(self) -> str:
        """Get the current turn's player who has to make choice. Returns the name of the player"""
        pass

    def get_player_one(self) -> str:
        """Get name of the player one"""
        pass

    def get_player_two(self) -> str:
        """Get name of the second player"""
        pass

    def draw_board(self):
        """Print out the tic tac toe board of given size to the terminal with selected choices"""
        pass

    def get_available_choices(self) -> list:
        """Get a list of choices avaiable for the player to select from"""
        pass

    def is_choice_available(self, choice: str) -> bool:
        """Check if a choice is available to be selected by the player"""
        pass

    def is_choice_valid(self, choice: str) -> bool:
        """Check if the choice selected by the player is valid. The choice must be one of the values from the list returned from get_available_choices"""
        pass

    def mark_choice(self, choice):
        """Mark choice on to the game board selected my the current player. Choice should be valid and available"""
        pass

    def get_winner(self) -> "tuple[bool, str]":
        """Get game status and winner in the form a tuple. Needs to be called after every mark_choice call"""
        pass

    def get_board_size(self) -> int:
        """Get the size of the board"""
        pass

    def get_winning_combinations(self) -> "list[tuple]":
        """Get a list of winning combination in the form of tuples"""
        pass

    def get_available_combinations(self) -> "list[tuple]":
        """Get a list of available combinations in the form of tuples"""
        pass

    def get_combination_weight(self, combination: "tuple[str]", search_symbol: str) -> int:
        """Get the weight of a combination in the game. Weight is calculated based on the number of consicutive repetetions of the search_symbol"""
        pass

    def get_computer_choice(self) -> str:
        """Get the computer's choice/move"""
        pass
