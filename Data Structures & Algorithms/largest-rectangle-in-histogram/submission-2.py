class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        n = len(heights)
        for i in range(n):
            start = i
            while stack and heights[stack[-1][1]] > heights[i]:
                index, height = stack.pop()
                area = (i - index) * heights[height]
                maxArea = max(maxArea, area)
                start = index
            stack.append([start, i])
        for i, heightidx in stack:
            area = (n - i) *  heights[heightidx]
            maxArea = max(maxArea, area)
        return maxArea