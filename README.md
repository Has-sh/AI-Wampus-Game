# Chocolate Game

## Description

This is a simple game where players take turns to eat chocolates from a board. The board also contains poison chocolates, which end the game if any are eaten. The game can be played in two modes:

1. **Human vs Human** - Two human players alternate turns to eat chocolates.
2. **Human vs AI** - A human player competes against an AI that uses the minimax algorithm to decide its moves.

## Features

- **Game Board Initialization**: The board is initialized with chocolates and poison chocolates based on user input.
- **Minimax Algorithm**: Used by the AI to determine the best move.
- **Human vs Human Mode**: Allows two players to take turns playing the game.
- **Human vs AI Mode**: Allows a human player to compete against an AI.

## Installation

To run the game, you need Python 3.6 or later. Clone the repository and run the main Python script.

```bash
git clone https://github.com/Has-sh/ChocolateGame.git
cd ChocolateGame
python chocolate_game.py
```

## Usage

1. **Initialization**:
   - Enter the number of rows and columns for the board.
   - Enter the row and column indices (1-based) where the poison chocolate is located.

2. **Game Mode Selection**:
   - Enter `1` for Human vs Human.
   - Enter `2` for Human vs AI.
   - If choosing Human vs AI, specify whether you want to start first or let the AI start.

3. **Playing the Game**:
   - For Human vs Human, players will be prompted to enter the row and column numbers to make a move.
   - For Human vs AI, the AI will make its move automatically.

4. **Game End**:
   - The game ends when a poison chocolate is eaten or no more valid moves are available.
   - The winner will be displayed at the end of the game.

## Functions

- `init_board(r, c)`: Initializes the board with chocolates and poison chocolates.
- `print_board()`: Displays the current state of the board.
- `is_game_over()`: Checks if the game is over based on the presence of eaten chocolates.
- `valid_row_and_column(row, col)`: Checks if the specified move is valid.
- `make_move(row, col)`: Makes a move by eating chocolates in the specified row and column.
- `minimax(is_maximizing)`: Minimax algorithm to determine the best move for the AI.
- `find_best_move()`: Finds the best move for the AI.
- `human_vs_human()`: Facilitates a game between two human players.
- `human_vs_ai(human_starts)`: Facilitates a game between a human player and the AI.

## Example

```
Enter number of rows: 5
Enter number of columns: 5
Enter the row of the poison chocolate (initial index = 1): 3
Enter the column of the poison chocolate (initial index = 1): 3
Enter game mode (1 for Human vs Human, 2 for Human vs AI): 2
Do you want to start first? (yes/no): yes
```

Enjoy!
