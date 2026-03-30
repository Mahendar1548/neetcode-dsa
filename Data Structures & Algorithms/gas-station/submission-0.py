class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas_value-cost_value for gas_value, cost_value in zip(gas, cost)]
        
        agg_diff = 0
        ans = -1
        for i in range(len(diff)):
            agg_diff += diff[i]
            if agg_diff < 0:
                ans = -1
            elif ans == -1:
                ans = i
        
        return ans
