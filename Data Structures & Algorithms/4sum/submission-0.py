class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j >= i + 2 and nums[j] == nums[j-1]:
                    continue
                start = j + 1
                end = n - 1
                while start < end:
                    sum_of_4 = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum_of_4 > target:
                        end -= 1
                        while start < end and nums[end+1] == nums[end]:
                            end -= 1
                    elif sum_of_4 <= target:
                        if sum_of_4 == target:
                            ans.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
        
        return ans