def next_move(player, board):
    def legal_moves(pos):
        """Return a list of legal moves for the given position."""
        i, j = pos
        moves = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue  # skip (0, 0)
                x, y = i + di, j + dj
                while 0 <= x < 10 and 0 <= y < 10 and board[x][y] == '-':
                    moves.append((x, y))
                    x += di
                    y += dj
        return moves

    def legal_shots(pos):
        """Return a list of legal shots for the given position."""
        i, j = pos
        shots = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue  # skip (0, 0)
                x, y = i + di, j + dj
                while 0 <= x < 10 and 0 <= y < 10 and board[x][y] in '-.':
                    shots.append((x, y))
                    x += di
                    y += dj
        return shots

    def minimax(player, depth, alpha, beta):
        """Minimax algorithm with alpha-beta pruning."""
        def score():
            """Evaluation function."""
            white_moves = sum(len(legal_moves((i, j))) for i in range(10) for j in range(10) if board[i][j] == 'W')
            black_moves = sum(len(legal_moves((i, j))) for i in range(10) for j in range(10) if board[i][j] == 'B')
            return white_moves - black_moves if player == 'W' else black_moves - white_moves

        def max_value(depth, alpha, beta):
            if depth == 0:
                return score()
            max_score = -float('inf')
            for i in range(10):
                for j in range(10):
                    if board[i][j] == player:
                        for move in legal_moves((i, j)):
                            x, y = move
                            board[i][j] = '-'
                            board[x][y] = player
                            for shot in legal_shots((x, y)):
                                a, b = shot
                                board[a][b] = '.'
                                max_score = max(max_score, min_value(depth - 1, alpha, beta))
                                board[a][b] = '-'
                                if max_score >= beta:
                                    board[x][y] = '-'
                                    board[i][j] = player
                                    return max_score
                                alpha = max(alpha, max_score)
                            board[x][y] = '-'
                            board[i][j] = player
            return max_score

        def min_value(depth, alpha, beta):
            if depth == 0:
                return score()
            min_score = float('inf')
            for i in range(10):
                for j in range(10):
                    if board[i][j] != player and board[i][j] != '-':
                        for move in legal_moves((i, j)):
                            x, y = move
                            board[i][j] = '-'
                            board[x][y] = board[i][j]
                            for shot in legal_shots((x, y)):
                                a, b = shot
                                board
