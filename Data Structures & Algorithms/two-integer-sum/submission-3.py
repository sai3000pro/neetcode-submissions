class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i, num in enumerate(nums):
            if (target - num) in myDict:
                return [myDict[target-num], i]
            else:
                myDict[num] = i
        
        