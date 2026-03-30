class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        curr = x
        sep = 1  if n % 2 else 1

        while n // 2:
            curr *= curr
            n //= 2
            if n % 2:
                sep *= x
                n -= 1
            # print(n, curr, sep)

        return curr * sep