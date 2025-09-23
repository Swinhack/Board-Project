def welcome():
    print("Welcome to Tic Tac Toe!")
    print("Player x goes first, then player 0")
    print("To make a move, enter the row and column numbers (1-3) when prompted.")


def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate (row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "
        print(row_str)
        if i != len(board) - 1:
            print("-----------")


def get_data (trun, board):
    while True:
        try:
            row_input = input("Row: ").strip()
            if not row_input:
                print("Input cannot be empty. Please enter a number from 1-3.")
                continue
            row = int(row_input)
            col_input = input("Column: ").strip()
            if not col_input:
                print("Input cannot be empty. Please enter a number from 1-3.")
                continue
            col = int(col_input)
        except ValueError:
            print("Invalid input, please enter numbers from 1-3.")
            continue
        if row < 1 or row > len(board):
            print ("Invalid row, try again")   
        elif col < 1 or col > len(board [row -1]):
            print ("Invalid column, try again")
        elif board [row -1][col -1] != " ":
            print ("Spot already taken, try again")
        else:
            board[row -1][col -1] = trun 
            break         


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            print(f"The winner is player {row[0]}")
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            print(f"The winner is player {board[0][col]}")
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(f"The winner is player {board[0][0]}")
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print(f"The winner is player {board[0][2]}")
        return True

    return False


def main():
    while True:
        board = [
            [" ", " ", " ",],
            [" ", " ", " ",],
            [" ", " ", " ",],
        ] 
        
        turn = "x".lower()
        turn_number = 0 
        welcome()  # Add this line to show the welcome message
        print_board(board)

        while turn_number < 9:
            print()
            print("It is the", turn, "players turn. Please select  your move.")
            get_data(turn, board)       
            print_board(board)

            if check_winner(board):
                break

            if turn == "x":
                turn = "0" 
            else:
                turn = "x" 
            turn_number += 1
        
if __name__ == "__main__":
    main()
print("Tied game")


# Game over, ask to play again
while True:
    play_game = input("Do you want to play again? (yes/no): ").lower()
    if play_game == "yes":
     print("Starting new game (Loading...)")
    elif play_game == "no":
        print("Thanks for playing")
    else:
        print("Invalid input, enter 'yes' or 'no'.")
        break