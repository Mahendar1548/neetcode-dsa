class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = dict()
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if not 0 <= i < len(s) or not 0 <= j < len(p):
                return False

            if (i, j) in cache:
                return cache[(i, j)]

            ans = False
            if p[j] == "*":
                ans = ans or dfs(i, j+1)
                if p[j-1] == "." or p[j-1] == s[i]:
                    ans = ans or dfs(i+1, j+1) or dfs(i+1, j)
            else:
                if s[i] == p[j] or p[j] == ".":
                    ans = ans or dfs(i+1, j+1)
            cache[(i, j)] = ans

            return ans

        return dfs(0, 0)

