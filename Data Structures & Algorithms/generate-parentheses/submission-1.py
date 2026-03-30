class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        def recur(open_b, close_b):
            if not open_b and not close_b:
                ans.append("".join(stack))
                return
            if open_b > 0:
                stack.append("(")
                recur( open_b-1, close_b)
                stack.pop()
            if close_b > open_b:
                stack.append(")")
                recur(open_b, close_b-1)
                stack.pop()

        recur(n, n)
        return ans
