class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_wise_index = dict()

        for index, value in enumerate(nums):
            if target - value in num_wise_index:
                return [num_wise_index[target-value], index]
            num_wise_index[value] = index