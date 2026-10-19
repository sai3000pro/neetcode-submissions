class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        while (i < n and intervals[i][1] < newInterval[0]):
            res.append(intervals[i]) # guarenteed to not be overlapping
            i += 1
        
        # now the next interval is overlapping, or could just be beyond
        while (i < n and intervals[i][0] <= newInterval[1]):
            # make use of newInterval!
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        res += intervals[i:]
        return res
            
