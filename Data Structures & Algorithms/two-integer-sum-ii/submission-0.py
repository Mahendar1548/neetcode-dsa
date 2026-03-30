class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 1
        right_pointer = len(numbers)
        
        while left_pointer < right_pointer:
            pointers_sum = numbers[left_pointer-1] + numbers[right_pointer-1]
            if pointers_sum == target:
                break
            elif pointers_sum > target:
                right_pointer -= 1
            else:
                left_pointer += 1

        return [left_pointer, right_pointer]
