class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temp_len = len(temperatures)
        ans = [0] * temp_len
        for i in range(temp_len-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        
        return ans
        