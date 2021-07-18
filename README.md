# Tic Tac Toe
A **`N*N`** Tic Tac Toe Game Written In Python.

![Animation](https://user-images.githubusercontent.com/10380630/126044261-d3337cc6-52c9-44f2-9d85-1910d3458fc4.gif)

#### Python Version: 3.8.5

#### How to run the Game
At the project root, run `python3 main.py` and follow the on-screen instructions.

#### How to run tests
At the project root, run `python3 test_tic_tac_toe_unittest.py` and follow the on-screen instructions.

#### Features
- N*N board size
- Play with computer

#### Steps To Play The Game
- Enter the size of the Tic Tac Toe Board (Minimum size is 3)
- Set Player One
- Set Player Two
- Set 1 for Player One two make the first move and 2 for the Second Player
- Set name COMP for any of the player to play with computer
- Enter the valid and available numbers marked inside the tic tac toe board cells to make move

#### Initializing The Game
```python
game = TicTacToe()
```
#### Setting the Tic Tac Toe Borad Size:
```python
game.set_board_size(size=3)
```
If the size if invalid number or less than 3 **`ValueError`**. 
      

#### Setting Players
```python
game.set_player_one(name="John")
game.set_player_two(name="Doe")
```
In case of same name for both the players or an empty name an **`Exception`** will be raised. To play with computer set name as **`COMP`**.

#### Selecting a player to make the first move
```python
game.first_choice_player(player='1')
```
pass 1 for the player one and 2 for the player two. Any other value will raise **`ValueError`**.

#### Drawing the Tic Tac Toe Board To Terminal
```python
game.draw_board()
```
#### Get size of the board
```python
game.get_board_size()
```
#### Showing Instructions
```python
game.show_instructions()
```
Prints instrcutions to the terminal window.

#### Getting the player who needs to make the current move
```python
game.get_turn()
```
#### Check if a choice is valid:
```python
game.is_choice_valid(choice='1')
```
Returns True in case of a valid choice else False. If board size is 3 then a choice should from 1,2,3,4,5,6,7,8,9 to be valid.

#### Check if a choice is available:
```python
game.is_choice_available(choice='1')
```
Check is a choice choosen by the player is available and not taken by the other player.

#### Making Move/Choice
```python
game.mark_choice(choice='1')
```
To make a move or choice.

#### Checking if the game is won
```python
game.get_winner()
```
Returns a tuple (True/False,'Name of the winner')

#### Get Winning Combinations
```python
game.get_winning_combinations()
```
Return a list of winning combinations in the form of tuples of length equal to the size of the board. Ex: `[('1','2','3'),('4','5','6')]`

#### Get Available Combinations
```python
game.get_available_combinations()
```
Return a list of available combinations in the form of tuples of length equal to the size of the board. Ex:Ex: `[('1','2','3'),('4','5','6')]`

#### Get Computer Choice
```python
game.get_computer_choice()
```
Returns a choice from the list of available choices. This method is useful when any of the player is **`COMP`**

#### Get Weight Of A Combination
```python
game.get_combination_weight(combination=('1','2','3'),search_symbol='X')
```
Valid values for `search_symbol` are `X` and `O`. A combination with higher weight has the more chance of winning the game. This method is used for computer making the choice.

### Interface
```python
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

```



