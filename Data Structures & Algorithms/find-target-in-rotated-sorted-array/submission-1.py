class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        

        start = low
        end = low + len(nums) - 1
        while start <= end:
            print(start, end)
            mid = (start + end) // 2
            mod_mid = mid % len(nums)
            if nums[mod_mid] == target:
                return mod_mid
            elif nums[mod_mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
            