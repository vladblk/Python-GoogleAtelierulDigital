import random

# board
board = ['_' for i in range(10)]


# display the board
def display_board(b) -> None:
    print(f'{b[1]} | {b[2]} | {b[3]}')
    print(f'{b[4]} | {b[5]} | {b[6]}')
    print(f'{b[7]} | {b[8]} | {b[9]}')

    return


# check if someone wins
def is_winner(b, p):
    line_1 = b[1] == p and b[2] == p and b[3] == p
    line_2 = b[4] == p and b[5] == p and b[6] == p
    line_3 = b[7] == p and b[8] == p and b[9] == p

    col_1 = b[1] == p and b[4] == p and b[7] == p
    col_2 = b[2] == p and b[5] == p and b[8] == p
    col_3 = b[3] == p and b[6] == p and b[9] == p

    diag_1 = b[1] == p and b[5] == p and b[9] == p
    diag_2 = b[7] == p and b[5] == p and b[3] == p

    return line_1 or line_2 or line_3 or col_1 or col_2 or col_3 or diag_1 or diag_2


def is_board_full(b):
    if b.count('_') > 1:
        return False
    else:
        return True


def player_move():
    is_valid = False

    while not is_valid:
        position = input('Select a position from 1-9: ')
        try:
            position = int(position)
            if 0 < position < 10:
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


def insert_position(position, p) -> None:
    board[position] = p
    return


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


main()
