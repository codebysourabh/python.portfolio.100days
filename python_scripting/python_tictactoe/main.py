# Create a 3x3 grid to represent the Tic Tac Toe board.
# - Initialize the board with empty spaces.
# - Display the initial empty board.
# - Repeat the following steps until the game is over:
#     - Player 1 makes a move:
#         - Prompt Player 1 to enter the row and column (1, 2, or 3) where - they want to place their 'X'.
#         - Update the board with 'X' at the specified position.
#         - Display the updated board.
#         - Check if Player 1 has won or if the board is full. If true, - end the game.
#     - b. Player 2 makes a move:
#         - Prompt Player 2 to enter the row and column (1, 2, or 3) where - they want to place their 'O'.
#         - Update the board with 'O' at the specified position.
#         - Display the updated board.
#         - Check if Player 2 has won or if the board is full. If true, - end the game.
# 
# If the game ends with a winner, declare the winner. If the game ends in a tie, declare a tie.

import game_art

print(game_art.logo)
print(game_art.game_instructions)
print("Player 1, you will be 'X', and Player 2 will be 'O'.")

def draw_board(board):
    # we are trying to print the board visually like
    # -------------
    # | 1 | 2 | 3 |
    # -------------
    # | 4 | 5 | 6 |
    # -------------
    # | 7 | 8 | 9 |
    # -------------
    
    row_seperator = "-" * 13 # 13 is the number of horizontal dashes used as row seperator
    print(row_seperator) 
    for i in range(3):
        # | 1 | 2 | 3 |
        print("|", board[ 0 + i * 3 ], "|", board[ 1 + i * 3 ], "|", board[ 2 + i * 3 ], "|" )
        print(row_seperator)


def player_input(board, token):
    
    valid_input = False
    while not valid_input:
        cell_num = input(f'where shall we put token: {token}? ')
        try:
            cell_num = int(cell_num)
        except ValueError:
            print(f'Invalid input, please check the value "{cell_num}", you entered.')
            continue
        
        if cell_num <= 0 or cell_num > 9:
            print("Invalid input, please enter a cell number between 1-9 that is not pre-occupied")
            continue
        
        if str(board[cell_num - 1]) not in "XO":
            board[cell_num - 1] = token
            valid_input = True
        else:
            print("This cell is already occupied, please enter a different cell numner between 1-9 that is not pre-occupied")

def check_win_condition(board_state):
    win_conditions = [(0,1,2), (3,4,5),(6,7,8), # horizontal
                      (0,3,6),(1,4,7),(2,5,8), # vertical
                      (0,4,8),(2,4,6)] # diagonal
    
    # checking if any of the win conditions are met by the board current state
    for condition in win_conditions:
        if board_state[condition[0]] == board_state[condition[1]] == board_state[condition[2]]:
            winning_token = board_state[condition[0]]
            return winning_token
    return False

def game_loop(board):    
    move_counter = 0
    game_on = True
    while game_on:
        draw_board(board)
        if move_counter % 2 == 0:
            player_input(board,'X')
        else:
            player_input(board,'O')
        move_counter += 1

        if 4 < move_counter < 9:
            game_state = check_win_condition(game_board)
            if game_state:
                print(f'We have a winner: {game_state}')
                game_on = False
                break
        if move_counter == 9:
            print(f'Game Draw! everyone wins!')
            break
    draw_board(board)
# initialise game board
game_board = list(range(1,10))
game_loop(game_board)
