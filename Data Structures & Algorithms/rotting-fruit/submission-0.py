from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        counter_nonrotten = 0
        max_time = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    counter_nonrotten += 1

        while queue:
            r, c, time = queue.popleft()
            if grid[r][c] == 2:
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            queue.append((new_r, new_c, time+1))      
                            max_time = max(max_time, time + 1)
                            counter_nonrotten -= 1

        return max_time if counter_nonrotten == 0 else -1