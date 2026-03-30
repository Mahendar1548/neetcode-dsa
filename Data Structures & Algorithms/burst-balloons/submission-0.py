class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        def dfs(nums_):
            nums_len = len(nums_)

            max_value = 0
            for i in range(nums_len):
                prev = nums_[i-1] if i > 0 else 1
                next_ = nums_[i+1] if i < nums_len -1 else 1
                nums_copy = nums_.copy()
                nums_copy.pop(i)
                value = prev*next_*nums_[i] + dfs(nums_copy)
                max_value = max(value, max_value)

            return max_value
        return dfs(nums)