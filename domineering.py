'''Complete the function nextMove that takes a char player and an 8x8 board as input to print the next move. 
Your output must be two integers with a single space separating them.'''

def nextMove(player, board):
    for i in range(8):
        for j in range(7):
            if player == 'v' and board[i][j] == '-' and board[i+1][j] == '-':
                print(i, j)
                return
            elif player == 'h' and board[j][i] == '-' and board[j][i+1] == '-':
                print(j, i)
                return
