class Solution:
    def checkValidString(self, s: str) -> bool:
        char_wise_count = defaultdict(int)
        for char in s:
            char_wise_count[char] += 1
            if char_wise_count["("] + char_wise_count["*"] < char_wise_count[")"]:
                return False
        if char_wise_count[")"] + char_wise_count["*"] < char_wise_count["("]:
            return False
        
        return True
