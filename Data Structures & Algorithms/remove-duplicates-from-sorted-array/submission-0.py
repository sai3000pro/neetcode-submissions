class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        n = len(nums)
        while fast < n:
            while fast < n and nums[slow] == nums[fast]:
                fast += 1 # skip it!
            if fast < n:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1