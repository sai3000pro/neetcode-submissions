from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            max_heap = [-stone for stone in stones]
            heapify(max_heap)
            while len(max_heap) > 1:
                x = heappop(max_heap) * -1
                y = heappop(max_heap) * -1
                if x != y:
                    x = max(x - y, y - x)
                    heappush(max_heap, x * -1)
            if max_heap == []:
                return 0
            else:
                return heappop(max_heap) * -1