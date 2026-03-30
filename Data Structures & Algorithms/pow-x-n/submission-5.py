class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        power = n
        n = abs(n)

        curr = x
        sep = 1

        while n:
            if n % 2:
                sep *= curr
            curr *= curr
            n //= 2

        return sep if power >=0 else 1/sep