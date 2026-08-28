class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # so just have a loop, and each element can be a starting point?
        n = len(nums)
        res = []
        def dfs(sol: List[int], picked: List[bool]) -> None:
            if len(sol) == n:
                res.append(list(sol))
            for i in range(n):
                if picked[i] == False:
                    sol.append(nums[i])
                    picked[i] = True
                    dfs(sol, picked)
                    sol.pop()
                    picked[i] = False
        dfs([], n * [False])
        return res