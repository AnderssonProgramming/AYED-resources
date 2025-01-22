from sys import stdin


def judge(board_game,  num_X, num_O):
    X_winner = 0
    O_winner = 0
    status = True

    for row in range(3):
        amount = sum(board_game[row])
        if amount == 3:
            X_winner += 1
        elif amount == 0:
            O_winner += 1

    for column in range(3):
        amount = 0
        for row in range(3):
            amount += board_game[row][column]
        if amount == 3:
            X_winner += 1
        elif amount == 0:
            O_winner += 1

    first_diagonal_amount = board_game[0][0] + board_game[1][1] + board_game[2][2]

    second_diagonal_amount = board_game[2][0] + board_game[1][1] + board_game[0][2]

    if first_diagonal_amount == 3 or second_diagonal_amount == 3:
        X_winner += 1
    elif first_diagonal_amount == 0 or second_diagonal_amount == 0:
       O_winner += 1

    if X_winner > 2 or O_winner > 2:
        status = False

    if len(board_game) != 3 and len(board_game) != 3:
        status = False

    if X_winner == 1 and O_winner == 1:
        status = False

    if O_winner == 1:
        if num_X - num_O != 0:
            status = False

    if X_winner >= 1:
        if num_X - num_O == 0:
            status = False

    if num_X - num_O > 1:
        status = False

    if num_O > num_X:
        status = False

    return status


def converter_count(board):
    num_X = 0
    num_O = 0
    for row in range(len(board)):
        for column in range((len(board[0]))):
            if board[row][column] == 'O':
                board[row][column] = 0
                num_O += 1
            elif board[row][column] == 'X':
                board[row][column] = 1
                num_X += 1
            elif board[row][column] == '.':
                board[row][column] = -3
    return board, num_X, num_O


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        board_game = []
        line = stdin.readline().strip().split()
        while line:
            board_game += [list(line[0])]
            line = stdin.readline().strip().split()
        board_game,  num_X, num_O = converter_count(board_game)
        if judge(board_game,  num_X, num_O):
            print("yes")
        else:
            print("no")



if __name__ == '__main__':
    main()
