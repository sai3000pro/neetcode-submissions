class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        if n == 0:
            return res
        numToAlpha = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
        5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 
        8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        def dfs(idx: int, sol: List[str]) -> None:
            if idx == n:
                res.append("".join(sol))
            else:
                letters = numToAlpha[int(digits[idx])]
                for letter in letters:
                    sol.append(letter)
                    idx += 1
                    dfs(idx, sol)
                    sol.pop()
                    idx -= 1
        dfs(0, [])
        return res