class Solution:
    def isHappy(self, n: int) -> bool:
        data = set()
        value = n
        while True:
            if value in data:
                return False
            data.add(value)
            sum_value = 0
            while value:
                sum_value += (value%10)**2
                value //= 10
            value = sum_value
            if value == 1:
                return True
        