class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCount = 0
        for num in nums:
            if num is not 0:
                totalProduct *= num
            else:
                zeroCount += 1
            if zeroCount > 1:
                return [0] * len(nums)
        
        res = []

        for num in nums:
            if zeroCount == 0:
                res.append(int(totalProduct / num))
            elif num != 0 and zeroCount == 1:
                res.append(0)
            else:
                res.append(totalProduct)                
        return res