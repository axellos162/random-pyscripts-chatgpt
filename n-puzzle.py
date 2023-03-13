from heapq import heappush, heappop
from collections import deque

class Board:
    def __init__(self, tiles, n, g=0, h=0, prev=None, move=None):
        self.tiles = tiles
        self.n = n
        self.g = g
        self.h = h
        self.prev = prev
        self.move = move
    
    def __lt__(self, other):
        return self.g + self.h < other.g + other.h
    
    def get_blank(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] == 0:
                    return (i, j)
    
    def get_neighbors(self):
        i, j = self.get_blank()
        neighbors = []
        if i > 0:
            new_tiles = [row[:] for row in self.tiles]
            new_tiles[i][j], new_tiles[i-1][j] = new_tiles[i-1][j], new_tiles[i][j]
            neighbors.append(Board(new_tiles, self.n, self.g+1, self.manhattan_distance(), self, "UP"))
        if i < self.n - 1:
            new_tiles = [row[:] for row in self.tiles]
            new_tiles[i][j], new_tiles[i+1][j] = new_tiles[i+1][j], new_tiles[i][j]
            neighbors.append(Board(new_tiles, self.n, self.g+1, self.manhattan_distance(), self, "DOWN"))
        if j > 0:
            new_tiles = [row[:] for row in self.tiles]
            new_tiles[i][j], new_tiles[i][j-1] = new_tiles[i][j-1], new_tiles[i][j]
            neighbors.append(Board(new_tiles, self.n, self.g+1, self.manhattan_distance(), self, "LEFT"))
        if j < self.n - 1:
            new_tiles = [row[:] for row in self.tiles]
            new_tiles[i][j], new_tiles[i][j+1] = new_tiles[i][j+1], new_tiles[i][j]
            neighbors.append(Board(new_tiles, self.n, self.g+1, self.manhattan_distance(), self, "RIGHT"))
        return neighbors
    
    def manhattan_distance(self):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] != 0:
                    x, y = divmod(self.tiles[i][j]-1, self.n)
                    distance += abs(x-i) + abs(y-j)
        return distance
    
    def is_goal(self):
        return self.manhattan_distance() == 0
    
    def get_path(self):
        path = []
        curr = self
        while curr.move:
            path.append(curr.move)
            curr = curr.prev
        return list(reversed(path))

def solve_puzzle(tiles, n):
    start = Board(tiles, n, h=tiles.manhattan_distance())
    visited = set()
    queue = []
    heappush(queue, start)
    
    while queue:
        curr = heappop(queue)
        visited.add(str(curr.tiles))
        if curr.is_goal():
            return curr.get_path()
        for neighbor in curr.get_neighbors():
            if str(neighbor.tiles) not in visited:
                heappush(queue, neighbor)
                
    return None

# Read input
n = int(input())
tiles = []
for i in range(n):
    row = list(map(int, input().split()))
    tiles.append(row)

# Solve puzzle
path = solve_puzzle(tiles, n)
if path is None:
    print("No solution found")
else:
    print("Moves to solve the puzzle:")
    for move in path:
        print(move)

