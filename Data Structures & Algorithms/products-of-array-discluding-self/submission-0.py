class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        product_from_right_side = [1] * nums_len
        value = 1
        for i in range(nums_len-2, -1, -1):
            print(value)
            value *= nums[i+1]
            product_from_right_side[i] = value
        
        print(product_from_right_side)
        
        product_from_left = 1
        ans = []
        for i in range(nums_len):
            ans.append(product_from_left*product_from_right_side[i])
            product_from_left *= nums[i]
        
        return ans
