class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recur(s, open, close):
            if not open and not close:
                ans.append(s)
                return
            if open > 0:
                recur(s + "(", open-1, close)
            if close > open:
                recur(s+")", open, close-1)
        
        recur("", n, n)
        return ans
