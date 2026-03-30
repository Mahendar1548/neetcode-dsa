class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        nums.sort()

        def dfs(idx):
            print(idx, curr)
            print("-" * 20)
            if idx >= len(nums):
                if curr not in ans:
                    ans.append(list(curr))
                return
            
            while idx < len(nums):
                curr.append(nums[idx])
                dfs(idx+1)
                curr.pop()
                while not curr and idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                    idx += 1
                dfs(idx + 1)
                idx += 1
        
        dfs(0)
        return ans
