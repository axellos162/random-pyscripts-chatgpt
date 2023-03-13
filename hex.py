from collections import deque
from itertools import product

# function to check if a path exists between two sides for a given player
def has_path(player, board):
    # define the start and end sides based on the player
    if player == 'R':
        start_side = 'left'
        end_side = 'right'
    else:
        start_side = 'top'
        end_side = 'bottom'
    
    # use DFS to find a path from the start side to the end side
    visited = set()
    stack = []
    # add cells in the start side to the stack
    if start_side == 'left':
        for i in range(len(board)):
            if board[i][0] == player:
                stack.append((i, 0))
    else:
        for j in range(len(board[0])):
            if board[0][j] == player:
                stack.append((0, j))
    # DFS loop
    while stack:
        i, j = stack.pop()
        # check if we have reached the end side
        if (end_side == 'right' and j == len(board[0])-1) or \
           (end_side == 'bottom' and i == len(board)-1):
            return True
        # mark the cell as visited
        visited.add((i, j))
        # add unvisited neighbors to the stack
        if i > 0 and (i-1, j) not in visited and board[i-1][j] == player:
            stack.append((i-1, j))
        if i < len(board)-1 and (i+1, j) not in visited and board[i+1][j] == player:
            stack.append((i+1, j))
        if j > 0 and (i, j-1) not in visited and board[i][j-1] == player:
            stack.append((i, j-1))
        if j < len(board[0])-1 and (i, j+1) not in visited and board[i][j+1] == player:
            stack.append((i, j+1))
    # no path found
    return False

# function to get the next move for a given player
def get_next_move(player, board):
    # try to find an unoccupied cell next to an occupied cell of the same player
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '-':
                if i > 0 and board[i-1][j] == player:
                    return chr(j+97) + str(i+1)
                if i < len(board)-1 and board[i+1][j] == player:
                    return chr(j+97) + str(i+1)
                if j > 0 and board[i][j-1] == player:
                    return chr(j+97) + str(i+1)
                if j < len(board[0])-1 and board[i][j+1] == player:
                    return chr(j+97) + str(i+1)
    # no unoccupied cell next to an occupied cell of the same player, try to find any unoccupied cell
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '-':
                return chr(j+97) + str(i+1)
    # board is full
    return None

# read input
player = input().strip()
board_size = int(input().strip())
board = []
for i in range(board_size):
    row = input().strip()
    board.append(row)

# define the board coordinates
coordinates = list(product('abcdefghijk', range(1, 12)))

# define the possible neighbor coordinates for each cell
neighbors = {coord: [c for c in [(chr(ord(coord[0]) - 1), coord[1]), 
                                 (chr(ord(coord[0]) - 1), coord[1] + 1),
                                 (coord[0], coord[1] - 1),
                                 (coord[0], coord[1] + 1),
                                 (chr(ord(coord[0]) + 1), coord[1] - 1),
                                 (chr(ord(coord[0]) + 1), coord[1])] if c in coordinates]
             for coord in coordinates}

# define the board and player information
player = input().strip()
rows = [input().strip() for _ in range(12)]
board = {coord: '-' if row[i] == '-' else None for i, coord in enumerate(coordinates) for row in rows}

# define the winning connections for both players
connections = {'R': [(coord, 'i') for coord in coordinates if coord[0] == 'a'],
               'B': [(coord, 'j') for coord in coordinates if coord[1] == 1]}

# define a helper function to get the player's connected components
def get_connected_components(player):
    connected = []
    visited = set()
    for coord, cell in board.items():
        if cell == player and coord not in visited:
            component = []
            queue = deque([coord])
            while queue:
                curr_coord = queue.popleft()
                if curr_coord not in visited:
                    visited.add(curr_coord)
                    component.append(curr_coord)
                    queue.extend(neighbors[curr_coord])
            connected.append(component)
    return connected

# define a helper function to check if the player has won
def has_won(player):
    for connection in connections[player]:
        if connection[0] in get_connected_components(player):
            return True
    return False

# define the starting player
current_player = 'R' if player == 'B' else 'B'

# keep playing until one player wins
while True:
    # print the current board
    for row in range(1, 12):
        print(' ' * (row - 1), end='')
        for col in range(1, 12):
            print(board[(chr(ord('a') + col - 1), row)] or '-', end=' ')
        print()
    
    # check if the current player has won
    if has_won(current_player):
        print(current_player + ' has won!')
        break
    
    # get the current player's move
    move = input().strip()
    
    # check if the move is valid
    if move not in coordinates or board[move] is not None:
        print('Invalid move. Try again.')
        continue
    
    # update the board with the current player's move
    board[move] = current_player
    
    # switch to the other player
    current_player = 'R' if current_player == 'B' else 'B'

