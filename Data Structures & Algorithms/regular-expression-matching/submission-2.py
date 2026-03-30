class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = dict()
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if not 0 <= j < len(p):
                return False

            if (i, j) in cache:
                return cache[(i, j)]

            ans = False
            if j+1 < len(p) and p[j+1] == "*":
                ans = ans or dfs(i, j+2)
                if 0 <= i < len(s) and (p[j] == "." or p[j] == s[i]):
                    ans = ans or dfs(i+1, j+2) or dfs(i+1, j)
            else:
                if 0 <= i < len(s) and (s[i] == p[j] or p[j] == "."):
                    ans = ans or dfs(i+1, j+1)
            cache[(i, j)] = ans

            return ans

        return dfs(0, 0)

