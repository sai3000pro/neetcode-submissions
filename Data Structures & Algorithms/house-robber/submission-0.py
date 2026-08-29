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
        i = n - 1
        while i > -1:
            if (i > 1) and (dp[i] == dp[i-2] + nums[i]):
                ans += nums[i] # optimal!
                i -= 2
            elif i == 1 or i == 0:
                ans += dp[i]
                i -= 2
            else:
                i -= 1
        return ans


            