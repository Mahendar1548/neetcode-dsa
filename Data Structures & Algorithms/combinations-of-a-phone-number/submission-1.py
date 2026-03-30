class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_wise_chars = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        ans = []
        str_len = len(digits)
        def dfs(curr_str, i):
            if i >= str_len:
                ans.append(curr_str)
                return

            for char in num_wise_chars[digits[i]]:
                dfs(curr_str+char, i+1)

        if digits:
            dfs("", 0)
        return ans

