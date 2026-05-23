class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        maxArea = 0
        currArea = 0

        def dfs(r, c):
            nonlocal currArea
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            if grid[r][c] == 1:
                grid[r][c] = 0
                currArea += 1
            else:
                return

            for dirRow, dirCol in directions:
                dfs(r + dirRow, c + dirCol)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    dfs(r, c)
                    maxArea = max(maxArea, currArea)
                    currArea = 0
        
        return maxArea
        
