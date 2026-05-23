class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        prefixHeight = [0] * n
        suffixHeight = [0] * n
        maxHeight = 0
        prefixHeight[0] = height[0]
        for i in range(len(height)- 1):
            maxHeight = max(maxHeight, height[i])
            prefixHeight[i] = maxHeight
        maxHeight = 0
        for i in range(len(height)- 1, 0, -1):
            maxHeight = max(maxHeight, height[i])
            suffixHeight[i] = maxHeight

        for i in range(len(height) - 1):
            area += max(0, min(prefixHeight[i], suffixHeight[i]) - height[i])
        return area
