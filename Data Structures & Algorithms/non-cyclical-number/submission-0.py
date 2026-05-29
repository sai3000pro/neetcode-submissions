class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        cycle.add(n)
        while n != 1:
            curr = n
            sum = 0
            while curr > 9:
                digit = curr % 10
                sum += digit ** 2
                curr = curr // 10
            sum += curr ** 2
            n = sum
            if n in cycle:
                return False
            cycle.add(n)
        return True
