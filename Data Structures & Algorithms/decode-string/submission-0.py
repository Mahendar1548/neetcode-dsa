class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
                continue
            
            curr_str = ""
            while stack[-1] != "[":
                curr_str = stack.pop() + curr_str
            stack.pop()
            
            num = 0
            pow_value = 0
            while stack and stack[-1].isdigit():
                num += int(stack.pop()) * (10**pow_value)
                pow_value += 1
            stack.append(curr_str*num)
        
        return "".join(stack)