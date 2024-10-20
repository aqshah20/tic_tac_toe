# Declare Board
from termcolor import colored

X = "X"
O = "O"
EMPTY = " "

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def cell(mark):
    """
    Format a cell in the board.

    :param mark: The mark to colorize, either "X" or "O".
    :return: A colored string representing the cell.
    """
    color = "green" if mark == X else "red"
    return colored(mark, color)


def print_board(board):
    """
    Print the current state of the board.

    :param board: A 3x3 2D list of strings, where each string is either "X", "0", or " " (space).
    :return: None
    """
    line = "---X---X---"
    print(line)

    for row in board:
        print(F' {cell(row[0])} | {cell(row[1])} | {cell(row[2])} ')
        print(line)


def check_winner(board):
    """
    Check if there is a winner in the game.

    :param board: A 3x3 2D list of strings, where each string is either "X", "0", or " " (space).
    :return: True if there is a winner, False otherwise.
    """
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return True

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != EMPTY:
            return True

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True

    return False


def is_full(board):
    """
    Check if the board is full.

    :param board: A 3x3 2D list of strings, where each string is either "X", "0", or " " (space).
    :return: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def get_position(prompt):
    """
    Get a position from the user.

    Repeatedly ask the user for a position until a valid number is entered.
    A valid position is when the number is between 0 and 2, inclusive.

    :param prompt: The prompt to give to the user.
    :return: The position as an int.
    """

    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print("Please enter a number")


def get_move(current_player):
    """
    Get the move from the user.

    Print whose turn it is, then repeatedly ask the user for a row and column
    until a valid move is entered. A valid move is when the spot is empty.

    :param current_player: The current player, either "X" or "0".
    :return: None
    """
    print(F"{current_player}'s turn")
    while True:
        row = get_position("Enter Row (0-2): ")
        column = get_position("Enter Column (0-2): ")

        if board[row][column] == " ":
            board[row][column] = current_player
            break

        print("This spot is already token")


def main():
    """
    Run the main game loop.

    Print the initial state of the board, then repeatedly ask the current player
    for a row and column, validate the input, update the board, and print the
    updated board. The loop continues indefinitely until the user stops it.

    :return: None
    """
    print_board(board)
    current_player = X

    while True:

        get_move(current_player)

        print_board(board)

        if check_winner(board):
            print(F"{current_player} wins!")
            break

        if is_full(board):
            print("Board is full!")
            break

        current_player = O if current_player == X else X


if __name__ == "__main__":
    main()
