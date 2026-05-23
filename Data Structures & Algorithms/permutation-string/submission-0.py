class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1chars = [0] * 26
        s1charSet = set(s1)
        for c in s1:
            s1chars[ord(c) - ord('a')] += 1
        s2charCount = defaultdict(int)
        currChars = 0
        start = 0
        for i, c in enumerate(s2):
            if c not in s1charSet:
                s2charCount = defaultdict(int)
                currChars = 0
                start = i + 1
                continue
            s2charCount[c] += 1
            currChars += 1
            while s2charCount[c] > s1chars[ord(c) - ord('a')]:
                s2charCount[s2[start]] -= 1
                start += 1
                currChars -= 1
            
            if currChars == len(s1):
                print(c)
                return True
            
        return False