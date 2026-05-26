class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        width = len(grid)
        height = len(grid[0])
        counter = 0

        def dfs(i, j):
            if i < 0 or i >= width or j < 0 or j >= height:
                return

            if grid[i][j] == '1':
                grid[i][j] = '#'

                for w, h in directions:
                    dfs(i + w, j + h)


        for i in range(width):
            for j in range(height):
                if grid[i][j] == '1':
                    dfs(i,j)
                    counter += 1
        
        return counter

                