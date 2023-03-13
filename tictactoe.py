def nextMove(player, board):
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == player and board[i][2] == '_':
            print(i, 2)
            return
        elif board[i][1] == board[i][2] == player and board[i][0] == '_':
            print(i, 0)
            return
        elif board[i][0] == board[i][2] == player and board[i][1] == '_':
            print(i, 1)
            return
        # Check columns
        elif board[0][i] == board[1][i] == player and board[2][i] == '_':
            print(2, i)
            return
        elif board[1][i] == board[2][i] == player and board[0][i] == '_':
            print(0, i)
            return
        elif board[0][i] == board[2][i] == player and board[1][i] == '_':
            print(1, i)
            return
    # Check diagonals
    if board[0][0] == board[1][1] == player and board[2][2] == '_':
        print(2, 2)
        return
    elif board[1][1] == board[2][2] == player and board[0][0] == '_':
        print(0, 0)
        return
    elif board[0][0] == board[2][2] == player and board[1][1] == '_':
        print(1, 1)
        return
    elif board[0][2] == board[1][1] == player and board[2][0] == '_':
        print(2, 0)
        return
    elif board[1][1] == board[2][0] == player and board[0][2] == '_':
        print(0, 2)
        return
    elif board[0][2] == board[2][0] == player and board[1][1] == '_':
        print(1, 1)
        return
    # If no winning move, play in the center if possible
    if board[1][1] == '_':
        print(1, 1)
        return
    # Otherwise, play in a corner if possible
    if board[0][0] == '_':
        print(0, 0)
        return
    elif board[0][2] == '_':
        print(0, 2)
        return
    elif board[2][0] == '_':
        print(2, 0)
        return
    elif board[2][2] == '_':
        print(2, 2)
        return
