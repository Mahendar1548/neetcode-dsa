class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_dec_q = deque()
        ans = [0] * len(temperatures)
        
        for idx, temp in enumerate(temperatures):
            while mon_dec_q and mon_dec_q[-1][1] < temp:
                popped_data = mon_dec_q.pop()
                ans[popped_data[0]] = idx - popped_data[0]
            
            mon_dec_q.append((idx, temp))
        
        return ans
