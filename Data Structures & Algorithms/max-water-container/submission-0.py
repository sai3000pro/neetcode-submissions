class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1
        while l <= r:
            currWater = min(heights[l], heights[r]) * (r - l)
            maxWater = max(maxWater, currWater)
            if heights[l] > heights[r]: # really the only way to potentially get a larger value
                r -= 1
            else:
                l += 1
        return maxWater
            