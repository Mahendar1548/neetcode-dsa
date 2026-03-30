class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, k-1
        min_sum = 0
        for i in range(k):
            min_sum = min_sum + self._get_diff_value(arr[i], x)

        curr_sum = min_sum
        for i in range(k, len(arr)):
            curr_sum = curr_sum + self._get_diff_value(arr[i],x) - self._get_diff_value(arr[i-k],x)
            if curr_sum < min_sum:
                min_sum = curr_sum
                left = i-k+1
                right = i

        return arr[left:right+1]
    
    def _get_diff_value(self, num, x):
        return abs(num - x)