#Author: Dustin Ngo
#Date: 4/29/2015

import connectfour
from connectfour import RED, YELLOW, NONE, new_game_state, drop_piece, pop_piece, winning_player
from shared_functions import print_board, printing_turns


def user_column_input(game_state) -> int:
    try:
        column_number = int(input("What column would you like to work with? 1-7 Only: "))
        column_numer = column_number
        if column_number < 1 or column_number > 7:
            print("Column number can only be from 1 through 7.\n")
            column_number = user_column_input(game_state)
            return column_number
        else:
            return column_number
    except ValueError:
            print("Invalid Input, Try Again.\n")
            column_number = user_column_input(game_state)
            return column_number

def drop_or_pop_piece(game_state, column_number: int):
    while True:
        try:
            drop_pop = input("Would you like to drop or pop the piece? ")
            drop_pop = drop_pop.upper().strip()
            if (drop_pop == "DROP"):
                game_state = connectfour.drop_piece(game_state,column_number-1)
                return game_state
            if (drop_pop == "POP"):
                game_state = connectfour.pop_piece(game_state,column_number-1)
                return game_state
            else:
                print("Invalid input.\n")
                column_number = user_column_input(game_state)
        except ValueError:
            print("Column Number is Invalid. 1-7 Only.\n")
            column_number = user_column_input(game_state)
            column_number = int(input("What column would you like to work with? 1-7 Only: "))
        except connectfour.GameOverError:
            print("Game is over.\n")
            break
        except connectfour.InvalidMoveError:
            print("Invalid Move, Try Again.\n")
            column_number = user_column_input(game_state)
            column_number = int(input("What column would you like to work with? 1-7 Only: "))

def local_program():
    game_state = new_game_state()
    print("Welcome to the local version of Connect 4!")
    while True:
        if (winning_player(game_state) == NONE):
            printing_turns(game_state.turn) 
            user_column = user_column_input(game_state)
            game_state = drop_or_pop_piece(game_state, user_column)
            print_board(game_state)
        if (winning_player(game_state) == RED):
            print("Red is the winner!")
            break;
        if (winning_player(game_state) == YELLOW):
            print("Yellow is the winner!")
            break;
    input("Game Finished. Please press any key to exit.")
        
if __name__ == '__main__':
    local_program()


        
    

