from typing import *

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_wise_count = set()
        for value in nums:
            if value not in value_wise_count:
                value_wise_count.add(value)
            else:
                return True
        
        return False

