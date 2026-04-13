class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def dfs(idx):
            nonlocal ans
            if idx == len(nums):
                return
            tmp = []
            for ans_idx in range(len(ans)):
                for perm_idx in range(len(ans[ans_idx])+1):
                    curr = ans[ans_idx][:perm_idx] + [nums[idx]] + ans[ans_idx][perm_idx:]
                    if curr not in tmp:
                        tmp.append(curr)

            ans = tmp
            dfs(idx+1)
        
        dfs(0)
        return ans
