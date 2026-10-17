class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        curSum, maxSum = 0, 0
        left = 0
        n = len(nums)
        curSet = set()
        for right in range(n):
            while nums[right] in curSet or len(curSet) == k:
                curSet.remove(nums[left])
                curSum -= nums[left]
                left += 1
            curSum += nums[right]
            curSet.add(nums[right])
            if len(curSet) == k:
                maxSum = max(maxSum, curSum)
        return maxSum


