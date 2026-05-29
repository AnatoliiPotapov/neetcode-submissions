from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        rows, cols = len(heights), len(heights[0])
        output = []
        p_w = [[0 for i in range(cols)] for j in range(rows)]
        a_w = [[0 for i in range(cols)] for j in range(rows)]

        pacific = deque()
        atlantic = deque()

        for row in range(rows):
            pacific.append((row, 0))
            atlantic.append((row, cols-1))
        for col in range(cols):
            pacific.append((0, col))
            atlantic.append((rows-1, col))

        while pacific:
            r, c = pacific.popleft()
            if p_w[r][c] == 0:
                p_w[r][c] = 1
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] >= heights[r][c]:
                            pacific.append((nr, nc))

        while atlantic:
            r, c = atlantic.popleft()
            if a_w[r][c] == 0:
                a_w[r][c] = 1
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] >= heights[r][c]:
                            atlantic.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if p_w[r][c] and a_w[r][c]:
                    output.append([r,c])

        return output
