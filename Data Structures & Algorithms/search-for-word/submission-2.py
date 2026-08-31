class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        n = len(word)
        def dfs(visited: List[Tuple[int]], row, col, index) -> bool:
            if index == n:
                return True
            elif row < 0 or row >= ROWS:
                return False
            elif col < 0 or col >= COLS:
                return False
            else:
                res = False
                if (row, col) in visited:
                    return False
                if board[row][col] == word[index]:
                    visited.add((row, col))
                    res = dfs(visited, row + 1, col, index + 1) or dfs(visited, row, col + 1, index + 1) or dfs(visited, row - 1, col, index + 1) or dfs(visited, row, col - 1, index + 1)
                    visited.remove((row, col))
                return res

        for row in range(ROWS):
            for col in range(COLS):
                visited = set()
                if dfs(visited, row, col, 0):
                    return True
        return False