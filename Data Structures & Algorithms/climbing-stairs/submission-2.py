class Solution:
    def climbStairs(self, n: int) -> int:
        aux = [0] * n
        aux[0] = 1
        for i in range(1, n):
            if i == 1:
                aux[i] = 1 + aux[i-1]
            else:
                aux[i] = aux[i-1] + aux[i-2]
        return aux[n-1]
