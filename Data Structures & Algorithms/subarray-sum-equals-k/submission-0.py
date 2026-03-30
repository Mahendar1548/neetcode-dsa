class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        visited_count = {0:1}
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in visited_count:
                count += visited_count.get(curr_sum - k, 0)
            visited_count[curr_sum] = visited_count.get(curr_sum, 0) + 1
        return count