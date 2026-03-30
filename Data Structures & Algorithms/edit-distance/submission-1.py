class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = dict()

        def backtrack(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if j >= len(word2):
                return len(word1)-i if len(word1)-i >0 else 0 ;
            
            ans = min(
                backtrack(i+1, j+1) if (0 <= i < len(word1) and 0 <= j < len(word2) and word1[i] == word2[j]) else float("inf"),
                1 + backtrack(i, j+1),
                1 + backtrack(i+1, j) if 0 <= i < len(word1) else float("inf"),
                1 + backtrack(i+1, j+1)  if 0 <= i < len(word1) else float("inf")
            )
            dp[(i, j)] = ans
            return ans
        return backtrack(0, 0)

        