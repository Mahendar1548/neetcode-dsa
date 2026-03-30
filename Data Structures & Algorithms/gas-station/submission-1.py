class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        ans = -1
        agg = 0
        for idx in range(len(cost)):
            diff = gas[idx] - cost[idx]
            agg += diff
            if agg < 0:
                ans = -1
                agg = 0
            elif ans == -1:
                ans = idx

        return ans