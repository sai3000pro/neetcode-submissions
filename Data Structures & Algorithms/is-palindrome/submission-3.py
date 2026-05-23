class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if (self.alphaNum(s[i]) and self.alphaNum(s[j])):
                if s[i] != s[j]:
                    return False
                i = i + 1
                j = j - 1
            elif (self.alphaNum(s[i])):
                j = j - 1
            elif (self.alphaNum(s[j])):
                i = i + 1
            else:
                i = i + 1
                j = j - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))