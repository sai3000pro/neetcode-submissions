class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(idx: int, sol: List[int], total: int, target: int):
            if total == target:
                res.append(list(sol))
                return
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                sol.append(candidates[i])
                dfs(i + 1, sol, total + candidates[i], target)
                sol.pop()
                    
        dfs(0, [], 0, target)
        return res