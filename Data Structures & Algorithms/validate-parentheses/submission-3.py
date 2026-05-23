class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {'(': ')', '{': '}', '[': ']'}
        for letter in s:
            if letter in paren:
                stack.append(paren[letter])
            else:
                if stack and letter == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack