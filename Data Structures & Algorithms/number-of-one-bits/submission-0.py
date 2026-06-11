class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        number = str(bin(n))
        for c in number:
            if c == '1':
                res += 1
        
        return res