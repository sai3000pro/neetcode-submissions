class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force = loop thru i+1 to n each time and count the number of days
        # one stack.
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index, oldTemp = stack.pop()
                result[index] = i - index
            stack.append((i, temp)) 
        return result