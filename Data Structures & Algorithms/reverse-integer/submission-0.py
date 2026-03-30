class Solution:
    def reverse(self, x: int) -> int:
        max_value = (1 << 32 - 1)

        is_neg = x < 0
        x = abs(x)
        res = 0
        while x:
            res = (res*10) + (x%10)
            x = x//10
        
        res = 0 if res > max_value else res
        return res if not is_neg else -res

        