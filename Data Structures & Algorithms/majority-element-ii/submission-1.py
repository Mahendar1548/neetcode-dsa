from copy import deepcopy
from itertools import count
from typing import *
import heapq

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = dict()
        for num in nums:
            if num not in candidates:
                if len(candidates) < 2:
                    candidates[num] = 1
                else:
                    for candidate in candidates:
                        candidates[candidate] -= 1
            else:
                candidates[num] += 1

            for candidate in list(candidates):
                if candidates[candidate] == 0:
                    del candidates[candidate]

        ans = []
        for candidate in candidates:
            if nums.count(candidate) > len(nums)/3:
                ans.append(candidate)

        return ans
