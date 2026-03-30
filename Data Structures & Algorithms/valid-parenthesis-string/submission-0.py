class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = 0
        star_count = 0
        for char in s:
            if char == "(":
                left_count += 1
            elif char == ")":
                if left_count:
                    left_count -= 1
                elif star_count:
                    star_count -= 1
                else:
                    return False
            else:
                star_count += 1
        
        return star_count >= left_count
