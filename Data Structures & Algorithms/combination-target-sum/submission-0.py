class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def dfs(idx):
            if sum(curr) >= target or idx >= len(nums):
                if sum(curr) == target:
                    ans.append(list(curr))
                return
            
            curr.append(nums[idx])
            dfs(idx)
            curr.pop()
            dfs(idx+1)

        dfs(0)
        return ans