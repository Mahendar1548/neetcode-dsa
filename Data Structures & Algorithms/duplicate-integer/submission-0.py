from typing import *

from collections import Counter


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter_items = Counter(nums)
        if max(counter_items.values()) > 1:
            return True
        return False
