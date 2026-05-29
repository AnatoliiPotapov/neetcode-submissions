from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        not_surrounded = [['X' for i in range(cols)] for j in range(rows)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = deque()

        def is_inside(r,c):
            return 0 <= r < rows and 0 <= c < cols

        for r in range(rows):
            if board[r][0] == 'O' and not_surrounded[r][0] == 'X':
                queue.append((r,0))
            if board[r][cols-1] == 'O' and not_surrounded[r][cols-1] == 'X':
                queue.append((r,cols-1))

        for c in range(cols):
            if board[0][c] == 'O' and not_surrounded[0][c] == 'X':
                queue.append((0,c))
            if board[rows-1][c] == 'O' and not_surrounded[rows-1][c] == 'X':
                queue.append((rows-1,c))

        while queue:
            r, c = queue.popleft()
            if not_surrounded[r][c] == 'O':
                continue
            not_surrounded[r][c] = 'O'

            for dr, dc in directions:
                n_r, n_c = r+dr, c+dc
                if is_inside(n_r, n_c):
                    if board[n_r][n_c] == 'O' and not_surrounded[n_r][n_c] == 'X':
                        queue.append((n_r, n_c))

        for r in range(rows):
            for c in range(cols):
                board[r][c] = not_surrounded[r][c]
        