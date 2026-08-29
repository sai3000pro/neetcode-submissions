class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        n = len(nums)
        nums.sort()
        def dfs(idx: int, sol: List[int]):
            res.append(list(sol))
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                else:
                    sol.append(nums[i])
                    dfs(i+1, sol)
                    sol.pop()
        dfs(0, [])
        return res
