class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1

        for idx in range(len(digits)-1, -1, -1):
            value = digits[idx] + carry
            ans.append(value%10)
            carry = value // 10
        
        if carry:
            ans.append(carry)
        
        ans.reverse()
        return ans

        