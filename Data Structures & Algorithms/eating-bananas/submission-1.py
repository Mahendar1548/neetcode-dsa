class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        while low < high:
            mid = (low + high) // 2
            total_req = self._get_hours_required(mid, piles)
            if total_req > h:
                low = mid + 1
            elif total_req <= h:
                high = mid
        
        return high

    def _get_hours_required(self, k, piles):
        total_req = 0
        for i in piles:
            total_req += math.ceil(i/k)
        return total_req
