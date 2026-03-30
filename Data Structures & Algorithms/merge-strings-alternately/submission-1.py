class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        p1, p2 = 0, 0
        w1_len, w2_len = len(word1), len(word2)
        while p1 < w1_len and p2 < w2_len:
            ans.append(word1[p1])
            p1 += 1
            ans.append(word2[p2])
            p2 += 1
        
        if p1 < w1_len:
            while p1 < w1_len:
                ans.append(word1[p1])
                p1 += 1
        
        if p2 < w2_len:
            while p2 < w2_len:
                ans.append(word2[p2])
                p2 += 1
        
        return ''.join(ans)