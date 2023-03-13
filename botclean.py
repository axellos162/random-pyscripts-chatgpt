'''Complete the function next_move that takes in 3 parameters posr, 
posc being the co-ordinates of the bot's current position and board which 
indicates the board state to print the bot's next move.

The codechecker will keep calling the function next_move till the 
game is over or you make an invalid move.'''



def next_move(posr, posc, board):
    # Check if the current cell is dirty and clean it if it is
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    
    # Look for the nearest dirty cell in each direction
    nearest_dirt = {'LEFT': None, 'RIGHT': None, 'UP': None, 'DOWN': None}
    for i in range(posr, -1, -1):  # Look left
        if board[i][posc] == 'd':
            nearest_dirt['LEFT'] = (i, posc)
            break
    for i in range(posr, 5):  # Look right
        if board[i][posc] == 'd':
            nearest_dirt['RIGHT'] = (i, posc)
            break
    for j in range(posc, -1, -1):  # Look up
        if board[posr][j] == 'd':
            nearest_dirt['UP'] = (posr, j)
            break
    for j in range(posc, 5):  # Look down
        if board[posr][j] == 'd':
            nearest_dirt['DOWN'] = (posr, j)
            break
    
    # Determine the direction of the nearest dirty cell
    direction = max(nearest_dirt, key=lambda x: nearest_dirt[x] if nearest_dirt[x] is not None else (-1, -1))
    if nearest_dirt[direction] is not None:
        if direction == 'LEFT':
            print("LEFT")
        elif direction == 'RIGHT':
            print("RIGHT")
        elif direction == 'UP':
            print("UP")
        else:
            print("DOWN")
    else:
        # If there are no dirty cells, terminate the program
        return
