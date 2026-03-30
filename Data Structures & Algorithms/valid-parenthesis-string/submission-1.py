class Solution:
    def checkValidString(self, s: str) -> bool:
        right_count = 0
        star_count = 0

        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char == ")":
                right_count += 1
            elif char == "(":
                if right_count:
                    right_count -= 1
                elif star_count:
                    star_count -= 1
                else:
                    return False
            else:
                star_count += 1
        
        return star_count >= right_count
        