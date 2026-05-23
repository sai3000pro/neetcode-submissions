class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        my_set = set(nums)
        possibleStarters = []
        for num in nums:
            if (num - 1) not in my_set:
                possibleStarters.append(num)
        maxLen = 1
        currLen = 1
        for starter in possibleStarters:
            while (starter + 1) in my_set:
                currLen += 1
                starter += 1
            maxLen = max(maxLen, currLen)
            currLen = 1
        return maxLen