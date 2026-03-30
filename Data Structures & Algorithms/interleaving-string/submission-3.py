class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)

        if s1_len + s2_len != s3_len:
            return False

        dp = dict()

        def dfs(a_idx, b_idx, current_idx):
            if current_idx == s3_len:
                return True
            
            if (a_idx, b_idx) in dp:
                return dp[(a_idx, b_idx)]

            ans = False
            if a_idx < s1_len and s3[current_idx] == s1[a_idx]:
                ans = ans or  dfs(a_idx+1, b_idx, current_idx+1)
            if b_idx < s2_len and s3[current_idx] == s2[b_idx]:
                ans = ans or dfs(a_idx, b_idx+1, current_idx+1)

            dp[(a_idx, b_idx)] = ans
            return ans

        return dfs(0, 0, 0)