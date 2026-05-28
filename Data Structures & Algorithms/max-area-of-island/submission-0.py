class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_area = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            counter = 0
            
            if not (0 <= i < rows) or not (0 <= j < cols):
                return 0

            if grid[i][j] == 1:
                grid[i][j] = -1
                counter += 1

                for dims in directions:
                    counter += dfs(i + dims[0], j + dims[1])

            return counter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area