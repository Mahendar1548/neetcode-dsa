class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self._inner_search(nums, target, 0, len(nums) - 1)

    def _inner_search(self, nums: List[int], target: int, low, high) -> bool:
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                return self._inner_search(nums, target, low, mid - 1) or self._inner_search(nums, target, mid + 1, high)

        return False