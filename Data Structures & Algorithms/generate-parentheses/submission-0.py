class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        length = n * 2
        def dfs(sol: List[str], right: int, left: int):
            if len(sol) == n * 2:
                res.append("".join(sol))
                return
            if right < n:
                right += 1
                sol.append("(")
                dfs(sol, right, left)
                sol.pop()
                right -= 1
            if left < right:
                left += 1
                sol.append(")")
                dfs(sol, right, left)
                sol.pop()
                left -= 1

        dfs([], 0, 0)
        return res