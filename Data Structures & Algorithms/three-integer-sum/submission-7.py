class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        nums_len = len(nums)

        i = 0
        while i < nums_len:
            while 0 < i < nums_len and nums[i-1] == nums[i]:
                i += 1

            if not i < nums_len - 2:
                break

            left_pointer = i + 1
            right_pointer = nums_len - 1
            target = -1 * nums[i]
            while left_pointer < right_pointer:
                pointer_sum = nums[left_pointer] + nums[right_pointer]
                if pointer_sum < target:
                    left_pointer += 1
                elif pointer_sum > target:
                    right_pointer -= 1
                else:
                    triplets.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1
            i += 1
        return triplets
