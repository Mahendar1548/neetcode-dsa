import string
from typing import *
from collections import Counter, defaultdict, deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mon_q = deque()
        ans = []
        left = 0
        for i, value in enumerate(nums):
            while mon_q and mon_q[-1] < value:
                mon_q.pop()
            mon_q.append(value)
            if i -left + 1 == k:
                ans.append(mon_q[0])
                if nums[left] == mon_q[0]:
                    mon_q.popleft()
                left += 1
        
        return ans

