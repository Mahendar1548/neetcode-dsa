class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_wise_max = defaultdict(list)
        for idx, char in enumerate(s):
            char_wise_max[char] = idx
        
        ans = []
        max_pos = 0
        start = 0
        for idx, char in enumerate(s):
            max_pos = max(max_pos, char_wise_max[char])
            if idx < max_pos:
                continue
            else:
                ans.append(idx-start+1)
                start = idx + 1
                max_pos = idx + 1
        
        return ans