class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [each for each in range(1, n+1)]
        ans = []
        current = []

        def dfs(idx, curr_len):
            if curr_len == k:
                ans.append(list(current))
                return
            if idx == n:
                return

            for inner_idx in range(idx, n):
                current.append(nums[inner_idx])
                dfs(inner_idx+1, curr_len+1)
                current.pop()
        dfs(0, 0)
        return ans