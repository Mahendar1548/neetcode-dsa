class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []
        str_len = len(s)
        
        def dfs(idx):
            if idx >= str_len:
                res.append(curr.copy())
            
            for j in range(idx, str_len):
                if is_palindrome(s, idx, j):
                    curr.append(s[idx:j+1])
                    dfs(j + 1)
                    curr.pop()
        
        
        def is_palindrome(string, i, j):
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        dfs(0)
        return res