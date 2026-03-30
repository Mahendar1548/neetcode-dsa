class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for each in intervals:
            if not ans or ans[-1][1] < each[0]:
                ans.append(each)
            else:
                ans[-1] = (
                    [min(each[0], ans[-1][0]),
                     max(each[1], ans[-1][1])]
                )
        
        return ans