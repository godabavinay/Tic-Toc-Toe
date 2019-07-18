from IPython.display import clear_output
import random

# function to display the board


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

# function to select player mark


def player_marker():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# function to check win condition


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the top
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            # down the left
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            # down the right
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            # diagnol
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            # diagnol
            (board[3] == mark and board[5] == mark and board[7] == mark))


# function to check white-space at a particular position


def space_check(board, position):
    return board[position] == ' '

# function to check full board is filled or not


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# function to check player choice


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9): '))

    return position

# function to place player mark


def place_marker(board, marker, position):
    board[position] = marker

# function to select a player at random


def random_player():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# function to replay game


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# main program starts
print('Welcome to Tic-Tac-Toe!')

while True:
    # Reset the board
    board = [' '] * 10
    player1_marker, player2_marker = player_marker()
    turn = random_player()

    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    game_on = None

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn

            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulatons! Player1 the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulatons! Player2 won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
