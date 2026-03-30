class Solution:
    def getSum(self, a: int, b: int) -> int:
        is_add = (a >= 0 and b >= 0) or (a < 0 and b < 0)
        if not is_add:
            if abs(a) < abs(b):
                a, b = b, a
        is_positive = bool(a >= 0)
        a, b = abs(a), abs(b)
        result = 0
        carry = 0
        for i in range(31):
            a_bit = a & 1
            b_bit = b & 1
            if is_add:
                result |= (a_bit^b_bit^carry) << i
                carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
            else:
                if carry & 1:
                    if a_bit & 1:
                        if b_bit & 1:
                            result |= 1 << i
                        else:
                            carry = 0
                    else:
                        if not b_bit & 1:
                            result |= 1 << i
                else:
                    if b_bit&1:
                        if not a_bit & 1:
                            carry = 1
                            result |= 1 << i
                    else:
                        result |= a_bit << i
            # print(carry, result)
            a >>= 1
            b >>= 1
        
        return result if is_positive else -result
