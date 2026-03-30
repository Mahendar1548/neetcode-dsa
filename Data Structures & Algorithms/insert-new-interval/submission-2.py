class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        is_new_done = False
        for idx in range(len(intervals)):
            curr = intervals[idx]
            if curr[0] >= newInterval[0]:
                intervals.insert(idx, newInterval)
                break
        else:
            intervals.append(newInterval)
        ans = [intervals[0]]
        
        for curr in intervals:
            prev = ans[-1]
            if prev[-1] >= curr[0]:
                ans[-1] = [min(prev[0], curr[0]), max(prev[1], curr[1])]
            else:
                ans.append(curr)
                
        return ans