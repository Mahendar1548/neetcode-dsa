class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1
        if n == 0:
            return 1

        curr = x
        sep = 1 if n % 2 else 1

        while n not in (0, 1):
            if n % 2:
                sep *= x
            curr *= curr
            n //= 2

        return curr * sep
