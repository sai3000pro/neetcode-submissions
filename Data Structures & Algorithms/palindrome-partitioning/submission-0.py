class Solution:
    def isPalindrome(self, start: int, end: int, s: str) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def dfs(start: int, sol: List[str]):
            if start == n:
                res.append(list(sol))
            # make it so that we append only palindromes to sol
            for end in range(start, n):
                if self.isPalindrome(start, end, s):
                    sol.append(s[start: end+1])
                    dfs(end+1, sol)
                    sol.pop()
        dfs(0, [])
        return res