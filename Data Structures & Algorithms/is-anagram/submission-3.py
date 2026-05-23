class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        tester = {}
        for i in range(len(s)):
            tester[s[i]] = tester.get(s[i], 0) + 1        
        for i in range(len(t)):
            if (t[i] in tester and tester[t[i]] > 0):
                tester[t[i]] -= 1
            else:
                return False
        return True
        