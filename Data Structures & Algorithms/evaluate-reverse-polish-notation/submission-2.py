class Solution:
    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_integer(token):
                stack.append(int(token))
            else:
                print(stack)
                b = stack.pop()
                a = stack.pop()
                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
        return int(stack[-1])