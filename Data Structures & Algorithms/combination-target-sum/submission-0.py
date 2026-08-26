class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def dfs(attempt: List[int], idx: int, total: int, target: int) -> None:
            if total == target:
                res.append(list(attempt))
                return
            for i in range(idx, n):
                if (nums[i] + total > target):
                    break
                attempt.append(nums[i])
                dfs(attempt, i, total + nums[i], target)
                attempt.pop()
        dfs([], 0, 0, target)
        return res
