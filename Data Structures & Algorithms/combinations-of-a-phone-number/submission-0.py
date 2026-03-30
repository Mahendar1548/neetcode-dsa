class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_wise_chars = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        ans = [""]
        str_len = len(digits)
        def dfs(i):
            nonlocal ans
            if i >= str_len:
                return
            
            temp = []
            for data in ans:
                for char in num_wise_chars[digits[i]]:
                    temp.append(data+char)
            ans = temp
            dfs(i+1)
        
        dfs(0)
        return ans
