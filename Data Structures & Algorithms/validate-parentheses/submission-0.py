class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_wise_open = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in closed_wise_open:
                if not stack or stack.pop() != closed_wise_open[char]:
                    return False
            else:
                stack.append(char)
        
        return False if stack else True

