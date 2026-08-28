class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # so just have a loop, and each element can be a starting point?
        n = len(nums)
        res = []
        def dfs(idx: int, sol: List[int], picked: List[bool]) -> None:
            if len(sol) == n:
                res.append(list(sol))
            for i in range(n):
                if picked[i] == False:
                    sol.append(nums[i])
                    picked[i] = True
                    dfs(i + 1, sol, picked)
                    sol.pop()
                    picked[i] = False
        dfs(0, [], n * [False])
        return res