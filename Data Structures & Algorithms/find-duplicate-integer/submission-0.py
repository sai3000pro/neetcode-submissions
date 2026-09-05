class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                return num
            