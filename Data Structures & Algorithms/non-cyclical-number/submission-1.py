class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        slow, fast = n , self._get_sum_of_squares(n)

        while slow != fast:
            slow = self._get_sum_of_squares(slow)
            fast = self._get_sum_of_squares(self._get_sum_of_squares(fast))
            if slow == 1 or fast == 1:
                return True
        
        return False


    def _get_sum_of_squares(self, num):
        value = 0
        while num:
            value += (num%10) ** 2
            num //= 10

        return value
