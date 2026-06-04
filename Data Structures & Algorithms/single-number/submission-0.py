class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # cannot sort
        # cannot use extra space... like a set
        res = 0
        for num in nums:
            res ^= num
        return res