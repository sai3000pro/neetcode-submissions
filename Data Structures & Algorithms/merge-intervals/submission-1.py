class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            last_added = res[-1]
            if interval[0] <= last_added[1]:
                last_added[1] = max(last_added[1], interval[1])
            else:
                res.append(interval)
        return res