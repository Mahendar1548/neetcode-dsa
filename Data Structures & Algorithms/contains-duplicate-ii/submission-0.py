class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_wise_idx = dict()
        for i in range(len(nums)):
            if nums[i] in num_wise_idx:
                if i - num_wise_idx[nums[i]] <= k:
                    return True
                
            num_wise_idx[nums[i]] = i
        
        return False