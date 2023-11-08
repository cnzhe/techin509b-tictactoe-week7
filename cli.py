# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import make_empty_board, get_winner, other_player
import logging

# Configure the logging settings
logging.basicConfig(
    filename = 'logs/tic_tac_toe.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for i, row in enumerate(board):
        formatted_row = [cell if cell is not None else ' ' for cell in row]
        print(" | ".join(formatted_row))
        if i < 2:  # Add two dashes below the first and second rows
            print("-" * 9)

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'  # Player 'X' starts
    moves = 0  # Track the number of moves

    while winner is None and moves < 9:  # Stop the game after 9 moves (a full board)
        # Show the board to the user.
        print_board(board)
        print(f"Player {player}'s turn.")
        
        # Input a move from the player.
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        # Check if the selected cell is empty
        if board[row][col] is not None:
            print("Invalid move. Cell already occupied.")
            continue

        # Log the player's move
        logging.info(f"Player {player} made a move at row {row}, column {col}.")

        # Update the board.
        board[row][col] = player

        # Update who's turn it is.
        player = other_player(player)
        moves += 1

        # Check for a winner
        winner = get_winner(board)

    # Show the final board to the user.
    print_board(board)

    if winner == 'X':
        logging.info("Player X won the game!")
        print("Player X won!")
    elif winner == 'O':
        logging.info("Player O won the game!")
        print("Player O won!")
    else:
        logging.info("The game ended in a draw.")
        print("It's a draw!")