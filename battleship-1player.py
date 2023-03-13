import random

# Define ship sizes
SHIPS = {
    'Submarine': 2,
    'Destroyer': 3,
    'Cruiser': 4,
    'Battleship': 5,
    'Carrier': 6,
}

# Define board size
N = 10

# Initialize board and ships
board = [['-' for _ in range(N)] for _ in range(N)]
ships = []

# Place ships randomly on board
for name, size in SHIPS.items():
    while True:
        # Choose orientation and position for ship
        is_horizontal = random.choice([True, False])
        if is_horizontal:
            row = random.randrange(N)
            col = random.randrange(N - size + 1)
        else:
            row = random.randrange(N - size + 1)
            col = random.randrange(N)
        # Check if position is available
        if all(board[row][col+i] == '-' for i in range(size)):
            # Place ship on board
            for i in range(size):
                if is_horizontal:
                    board[row][col+i] = name[0]
                else:
                    board[row+i][col] = name[0]
            # Save ship position and orientation
            ships.append((name, row, col, is_horizontal))
            break

# Print board
print(' '.join(str(i) for i in range(N)))
for i, row in enumerate(board):
    print(i, ' '.join(str(c) for c in row))

# Play game
moves = 0
while ships:
    # Ask user for input
    row, col = input('Enter row and column to attack (e.g. 5 6): ').split()
    row, col = int(row), int(col)
    # Check if move is valid
    if not (0 <= row < N and 0 <= col < N):
        print('Invalid move, please try again.')
        continue
    if board[row][col] != '-':
        print('You already attacked this position, please try again.')
        continue
    # Update board and ships
    moves += 1
    hit = False
    for i, (name, r, c, is_horizontal) in enumerate(ships):
        if is_horizontal:
            if r == row and c <= col < c+len(name):
                board[row][col] = 'h'
                if all(board[row][c+i] == 'h' for i in range(len(name))):
                    print(f'{name} has been destroyed!')
                    for j in range(len(name)):
                        board[row][c+j] = 'd'
                    ships.pop(i)
                    hit = True
                break
        else:
            if r <= row < r+len(name) and c == col:
                board[row][col] = 'h'
                if all(board[r+i][col] == 'h' for i in range(len(name))):
                    print(f'{name} has been destroyed!')
                    for j in range(len(name)):
                        board[r+j][col] = 'd'
                    ships.pop(i)
                    hit = True
                break
    if not hit:
        print('Miss!')
        board[row][col] = 'm'
    # Print board
    print(' '.join(str(i) for i in range(N)))
    for i, row in enumerate(board):
        print(i, ' '.join(str(c) for c in row))

# Print score
score = (100 - moves) // 5
print(f'Congratulations, you won with a score of {score}!')
