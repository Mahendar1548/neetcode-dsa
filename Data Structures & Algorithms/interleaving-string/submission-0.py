class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        
        if s1_len + s2_len != s3_len:
            return False

        def dfs(a_idx, b_idx, current_str):
            if len(current_str) == s3_len:
                if current_str == s3:
                    return True
                return False
            
            ans = False
            if a_idx < s1_len:
                ans = ans or  dfs(a_idx+1, b_idx, current_str+s1[a_idx])
            if b_idx < s2_len:
                ans = ans or dfs(a_idx, b_idx+1, current_str+s2[b_idx])
            
            return ans
        
        return dfs(0, 0, "")
