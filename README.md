# Tic-Tac-Toe
(cs50:AI PROJECT)
Minimax, an IA to play Tic-Tac-Toe optimally.
![Example](game.png)

### Getting Started

Once in the directory for the project, run
```python
pip3 install -r requirements.txt
```
to install the required Python package (pygame) for this project.
then run
```python
python runner.py
```
to execute the game.
### Understanding

There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. runner.py has been implemented for you, and contains all of the code to run the graphical interface for the game. Once you’ve completed all the required functions in tictactoe.py, you should be able to run python runner.py to play against your AI!

Let’s open up tictactoe.py to get an understanding for what’s provided. First, we define three variables: X, O, and EMPTY, to represent possible moves of the board.

The function initial_state returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY.

* The *player* function takes a *board state* as input, and return which player’s turn it is (either X or O).
  * In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
  * if a terminal board is provided as input => the game is already over.
* The *actions* function returns a set of all of the possible actions that can be taken on a given board.
  * Each action is represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
  * Possible moves are any cells on the board that do not already have an X or an O in them.
  * if a terminal board is provided as input => the game is already over.
* The *result* function takes a board and an action as input, and returns a new board state, without modifying the original board.
  * If action is not a valid action for the board, the program will raise an exception.
  * The returned board state is the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
* The  *winner* function accepts a board as input, and returns the winner of the board if there is one.
  * If the X player has won the game, the function will return X. If the O player has won the game, the function will return O.
  * One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
  * If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function will return None.
* The *terminal* function should accept a board as input, and return a boolean value indicating whether the game is over.
  * If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the will function return True.
  * Otherwise, the function will return False if the game is still in progress.
* The *utility* function accepts a terminal board as input and output the utility of the board.
  * If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
  * utility will only be called on a board if terminal(board) is True.
* The *minimax* function takes a board as input, and returns the optimal move for the player to move on that board.
  * The returned move is the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
  * If the board is a terminal board, the *minimax* function will return None.
  
  
