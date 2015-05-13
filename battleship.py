__author__ = 'Alexis'
from random import randint
ROW_SIZE = 4
COL_SIZE = 4
NUM_SHIPS = 4
TURNS = 5

def setup_board():
    board = []
    for x in range(ROW_SIZE): #This changes the board size
        board.append(["O"] * COL_SIZE)
    print "Let's play Battleship!"
    print_board(board)
    return board


def print_board(board):
    for row in board:
        print " ".join(row)

def ship_generator(num_ships):
    ships = []
    for _ in range(num_ships):
        generate_coord = True
        while generate_coord:
            pot_coord = [randint(0, ROW_SIZE - 1), randint(0, COL_SIZE - 1)]
            overlaps = 0
            for ship in ships:
                if pot_coord == ship:
                    overlaps += 1
            if overlaps == 0:
                generate_coord = False
        # Definition of While Loops: The while loop runs as long as the condition is true until the condition is false. In this case, The While loop will run until it has no overlaps.
        ships.append(pot_coord)
    return ships


def play_game(board):
    ships = ship_generator(NUM_SHIPS)
    turn = 0
    for turn in range(TURNS): #This is the number of turns
        print "Turn", turn + 1
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        if [guess_row, guess_col] in ships:
        #If this element is in this array "then what?"
            print "Congratulations! You sunk my battleship!"
            board[guess_row][guess_col] = "T"
        else:
            if (guess_row < 0 or guess_row > ROW_SIZE - 1) or (guess_col < 0 or guess_col > COL_SIZE - 1): #Also change with board size
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == "X":
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
        print_board(board)


if __name__ == '__main__':
    board = setup_board()
    play_game(board)






