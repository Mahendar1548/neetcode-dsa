class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = 0
        right_count = 0
        for i in range(len(s)):
            left_char = s[i]
            right_char = s[len(s)-1-i]

            if left_char in ("(", "*"):
                left_count += 1
            else:
                left_count -= 1
            
            if right_char in (")", "*"):
                right_count += 1
            else:
                right_count -= 1
            
            if left_count < 0 or right_count < 0:
                return False
            print(i, len(s), left_count, right_count)
        
        return True
