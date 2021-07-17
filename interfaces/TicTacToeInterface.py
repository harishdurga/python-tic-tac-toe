class TicTacToeInterface:

    def set_board_size(self, size: int):
        pass

    def set_player_one(self, name: str):
        pass

    def set_player_two(self, name: str):
        pass

    def show_instructions():
        pass

    def first_choice_player(self, player: str):
        pass

    def get_turn(self) -> str:
        pass

    def get_player_one(self) -> str:
        pass

    def get_player_two(self) -> str:
        pass

    def draw_board(self):
        pass

    def get_available_choices(self) -> list:
        pass

    def is_choice_available(self, choice: str) -> bool:
        pass

    def is_choice_valid(self, choice: str) -> bool:
        pass

    def mark_choice(self, choice):
        pass

    def get_winner(self) -> "tuple[bool, str]":
        pass

    def get_board_size(self) -> int:
        pass

    def get_winning_combinations(self) -> "list[tuple]":
        pass
