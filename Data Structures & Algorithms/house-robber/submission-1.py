class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                dp[0] = num
            elif i == 1:
                dp[i] = max(num, dp[i-1]) # rob either last house or this house
            else:
                dp[i] = max(dp[i-1], num + dp[i-2]) # rob either this house and get the max you can from the previous houses, or don't rob
        return dp[-1]


            