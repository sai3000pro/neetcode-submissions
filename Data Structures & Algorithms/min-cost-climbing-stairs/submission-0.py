class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [0] * n
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        for i, c in enumerate(cost):
            if i > 1:
                minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
        return min(minCost[n-1], minCost[n-2])

