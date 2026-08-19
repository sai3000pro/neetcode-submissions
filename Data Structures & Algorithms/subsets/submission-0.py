class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(idx: int, curr: List[int]) -> None:
            res.append(list(curr))
            for i in range(idx, n):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        dfs(0, [])

        return res