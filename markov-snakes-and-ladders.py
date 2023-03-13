from random import choices

def play_game(prob, ladders, snakes):
    num_rolls = 0
    curr_pos = 1
    while curr_pos != 100:
        num_rolls += 1
        roll = choices([1,2,3,4,5,6], weights=prob)[0]
        new_pos = curr_pos + roll
        if new_pos > 100:
            continue
        for start, end in ladders:
            if new_pos == start:
                new_pos = end
                break
        for start, end in snakes:
            if new_pos == start:
                new_pos = end
                break
        curr_pos = new_pos
        if num_rolls >= 1000:
            break
    return num_rolls

def expected_num_rolls(prob, ladders, snakes):
    num_simulations = 5000
    num_rolls = 0
    for _ in range(num_simulations):
        num_rolls += play_game(prob, ladders, snakes)
    return int(num_rolls/num_simulations)

num_tests = int(input())
for i in range(num_tests):
    prob = [float(p) for p in input().split(',')]
    num_ls = input().split(',')
    num_ladders, num_snakes = int(num_ls[0]), int(num_ls[1])
    ladders = [tuple(map(int, input().split(','))) for _ in range(num_ladders)]
    snakes = [tuple(map(int, input().split(','))) for _ in range(num_snakes)]
    print(expected_num_rolls(prob, ladders, snakes))

# here's how this solution works
''' The play_game function simulates one game of snakes and ladders given the probabilities of the die, the positions of the ladders, and the positions of the snakes. 
It keeps rolling the die and moving the player's position until the player reaches square 100. 
It also checks if the player has landed on a ladder or a snake and updates the player's position accordingly. 
If the player hasn't reached square 100 after 1000 rolls, it terminates the game and ignores it.
The expected_num_rolls function simulates num_simulations games of snakes and ladders and returns the average number of rolls required to win the game. 
It simply calls the play_game function num_simulations times and takes the average of the number of rolls required to win each game.
The main program reads the input, calls the expected_num_rolls function for each test case, and prints the result. '''