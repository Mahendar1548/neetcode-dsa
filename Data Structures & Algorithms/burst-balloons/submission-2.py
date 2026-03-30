class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = dict()
        nums = [1] + nums + [1]
        def dfs(left, right):
            if (left, right) in dp:
                return dp[(left, right)]

            max_value = 0
            for i in range(left, right+1):
                prev = nums[left - 1]
                next_ = nums[right + 1]
                value = prev * next_ * nums[i] + dfs(left, i-1) + dfs(i+1, right)
                max_value = max(value, max_value)

            dp[(left, right)] = max_value
            return max_value

        return dfs(1, len(nums)-2)
