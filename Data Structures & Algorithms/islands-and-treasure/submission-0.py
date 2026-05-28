from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # populate queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        # do bfs
        while queue:
            r, c = queue.popleft()
            distance = grid[r][c]
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (0 <= new_r < rows and 0<= new_c < cols):
                    if grid[new_r][new_c] == INF:
                        grid[new_r][new_c] = distance + 1
                        queue.append((new_r, new_c))

