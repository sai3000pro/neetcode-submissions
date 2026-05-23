class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSet = set()
        boxSet = set()
        for rowNum, row in enumerate(board):
            for col, num in enumerate(row):
                if num == '.':
                    continue
                boxKey = (rowNum // 3) * 3 + (col // 3) # this works because 0 1 2, 3 4 5, 6 7 8 would be the keys
                if ((col, num) in colSet) or ((rowNum, num)) in rowSet or ((boxKey, num)) in boxSet:
                    return False
                else:
                    colSet.add((col, num))
                    rowSet.add((rowNum, num))
                    boxSet.add((boxKey, num))
        return True