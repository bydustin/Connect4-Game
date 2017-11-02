#Dustin Ngo (#77035127) & Lansen Zhao (Unknown)	

import connectfour
from connectfour import RED, YELLOW, NONE, new_game_state, drop_piece, pop_piece, winning_player

def print_board(game_state)-> None:
    for i in range(connectfour.BOARD_COLUMNS):
        print(i+1, end='  ')
    print()
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if game_state.board[column][row]== 0:
                print('.', end='  ')
            elif game_state.board[column][row]== 1:
                print('R', end='  ')
            elif game_state.board[column][row]== 2:
                print('Y', end='  ') 
        print()


def printing_turns(turn):
    if (turn == RED):
        print("\nIt is now red's turn.\n")
    elif (turn == YELLOW):
        print("\nIt is now yellow's turn.\n")
    return turn

    
