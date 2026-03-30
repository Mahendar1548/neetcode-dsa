class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_val = 0
        for idx, value in enumerate(heights):
            current_value_idx_for_stack = idx
            while stack and stack[-1][1] > value:
                pop_idx, pop_val = stack.pop()
                current_value_idx_for_stack = pop_idx
                max_val = max(max_val, (idx - pop_idx) * pop_val)
                print(pop_idx, pop_val, max_val)
            stack.append((current_value_idx_for_stack, value))
        
        while stack:
            pop_idx, pop_val = stack.pop()
            max_val = max(max_val, (len(heights) - pop_idx) * pop_val)
            print(pop_idx, pop_val, max_val)
        return max_val
