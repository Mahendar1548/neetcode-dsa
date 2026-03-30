from typing import *
from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        num_wise_freq = Counter(nums)
        freq_wise_nums = defaultdict(list)
        for num, freq in num_wise_freq.items():
            freq_wise_nums[freq].append(num)

        rem_to_fill = k
        ans = []
        for i in range(nums_len, 0, -1):
            if i in freq_wise_nums:
                ans.extend(freq_wise_nums[i][:rem_to_fill])
                rem_to_fill -= len(freq_wise_nums[i])
            if rem_to_fill <= 0:
                break

        return ans
