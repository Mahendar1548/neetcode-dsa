class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ss = []

        def dfs(idx):
            if idx >= len(nums):
                ans.append(list(ss))
                return
            
            ss.append(nums[idx])
            dfs(idx+1)
            ss.pop()
            dfs(idx+1)
        
        dfs(0)
        return ans