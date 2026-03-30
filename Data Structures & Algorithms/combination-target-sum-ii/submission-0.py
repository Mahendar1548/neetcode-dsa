class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        candidates.sort()
        
        def backtrack(idx, total_sum):
            if total_sum >= target:
                if target == total_sum:
                    ans.append(list(curr))
                return 
            
            if idx >= len(candidates):
                return
            
            curr.append(candidates[idx])
            total_sum += candidates[idx]
            backtrack(idx+1, total_sum)
            curr.pop()
            total_sum -= candidates[idx]
            
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            
            backtrack(idx+1, total_sum)
        
        backtrack(0, 0)
        return ans