class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        def dfs(x, y):
            neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for r, c in neighbours:
                if r >= 0  and c >= 0 and r < ROWS and c < COLS:
                    if grid[r][c] == "1":
                        grid[r][c] = "0"
                        dfs(r, c)
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    grid[r][c] = "0"
                    dfs(r, c)
        
        return islands
