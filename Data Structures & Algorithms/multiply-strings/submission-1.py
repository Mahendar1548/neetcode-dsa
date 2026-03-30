class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_len, num2_len = len(num1), len(num2)
        res = [0] * (num1_len+num2_len)
        
        for i in range(num1_len-1, -1, -1):
            idx = (num1_len+num2_len-1) - (num1_len-1-i)
            carry = 0
            for j in range(num2_len-1, -1, -1):
                num1_val = ord(num1[i]) - ord("0")
                num2_val = ord(num2[j]) - ord("0")
                pro_val = num1_val * num2_val
                total = pro_val + res[idx] + carry
                res[idx] = total % 10
                carry = total // 10
                idx -= 1
            while carry:
                total = res[idx] + carry
                res[idx] = total % 10
                carry = total // 10
                idx -= 1
        ans = ""
        val_start = False
        for idx in range(num1_len+num2_len):
            if not val_start and not res[idx]:
                continue
            ans += str(res[idx])
        
        return ans if ans else "0"