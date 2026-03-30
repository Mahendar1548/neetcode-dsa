class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = sum(weights)//days, sum(weights)
        while low < high:
            mid = (low + high) // 2
            can_ship = self._can_ship(weights, mid, days)
            if can_ship:
                high = mid
            else:
                low = mid + 1

        return high


    def _can_ship(self, weights: List[int], weight, days) -> bool:
        req_days = 0
        i = 0
        no_of_weights = len(weights)
        while i < no_of_weights and req_days <= days:
            curr = 0
            while i < no_of_weights and (curr + weights[i] <= weight):
                curr += weights[i]
                i += 1
            req_days += 1
        return req_days <= days