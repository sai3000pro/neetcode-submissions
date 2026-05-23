class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "*" + string
        return res
    def decode(self, s: str) -> List[str]:
        temp = ""
        res = []
        i = 0
        while i < len(s):
            if s[i] == "*":
                lengthofstr = int(temp)
                res.append(s[i+1:i+lengthofstr+1])
                temp = ""
                i += lengthofstr
            else:
                temp += s[i]
            i += 1
        return res