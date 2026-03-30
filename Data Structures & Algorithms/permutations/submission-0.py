class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(idx):
            if idx >= len(nums) - 1:
                ans.append(list(nums))
                return
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        dfs(0)
        return ans
        