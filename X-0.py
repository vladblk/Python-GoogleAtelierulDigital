import random

# board
board = ['_' for i in range(10)]

# display the board
def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')


# check if someone wins
def is_winner(board, p):
    return (board[1] == p and board[2] == p and board[3] == p) or (board[4] == p and board[5] == p and board[6] == p) or (board[7] == p and board[8] == p and board[9] == p) or (board[1] == p and board[4] == p and board[7] == p) or (board[2] == p and board[5] == p and board[8] == p) or (board[3] == p and board[6] == p and board[9] == p) or (board[1] == p and board[5] == p and board[9] == p) or (board[7] == p and board[5] == p and board[3] == p)


def is_board_full(board):
    if board.count('_') > 1:
        return False
    else:
        return True


def player_move():
    is_valid = False

    while not is_valid:
        position = input('Select a position from 1-9: ')
        try:
            position = int(position)
            if position > 0 and position < 10:
                if is_position_free(position):
                    is_valid = True
                    return position
                else:
                    print('Position is taken')
            else:
                print('Select a position from 1-9')

        except ValueError:
            print('Please insert a number')



def computer_move():
    all_possible_positions = [i for i, j in enumerate(board) if j == '_' and i != 0]

    position = 0

    # MAKE COMPUTER TAKE WINNING MOVE OR BLOCK THE PLAYER FROM WINNING
    # for p in ['0', 'X']:
    #     for i in all_possible_positions:
    #         board_copy = board[:]
    #         board_copy[i] = p
    #
    #         if is_winner(board_copy, p):
    #             position = i
    #             return position

    # poziția 5 este cea mai vânată
    if 5 in all_possible_positions:
        position = 5
        return position

    # poziția 1 sau 3 sau 7 sau 9 reprezintă opțiunea a doua în cerință calculatorului
    second_option = []
    for i in all_possible_positions:
        if i in [1, 3, 7, 9]:
            second_option.append(i)

    if len(second_option) > 0:
        position = random.choice(second_option)
        return position

    # în cazul în care toate acestea sunt ocupate se încearcă prima valoare rămasă libere dintre 2, 4, 6, 8
    third_option = []
    for i in all_possible_positions:
        if i in [2, 4, 6, 8]:
            third_option.append(i)

    if len(third_option) > 0:
        position = random.choice(third_option)
        return position

    return position


def insert_position(position, p):
    board[position] = p


def is_position_free(pos):
    return board[pos] == '_'


def main():
    display_board(board)

    while not is_board_full(board):
        if not is_winner(board, '0'):
            position = player_move()
            insert_position(position, 'X')
            display_board(board)
        else:
            print('Computer wins!')
            break

        if not is_winner(board, 'X'):
            position = computer_move()

            if position == 0:
                print('Tie')
            else:
                insert_position(position, '0')
                print(f'Computer inserted \'0\' at position: {position}')
                display_board(board)
        else:
            print('Player wins!')
            break

    if is_board_full(board):
        print('Tie')


main()