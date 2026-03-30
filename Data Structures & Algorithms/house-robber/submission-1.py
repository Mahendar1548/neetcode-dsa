class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for value in nums:
            temp = max(rob1+value, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
