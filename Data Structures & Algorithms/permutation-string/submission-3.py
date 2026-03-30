class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[self.get_idx(s1[i])] += 1
            s2_count[self.get_idx(s2[i])] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0
        
        start = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            char_idx = self.get_idx(s2[i])
            if s1_count[char_idx] == s2_count[char_idx]:
                matches -= 1
            elif s1_count[char_idx] == 1 + s2_count[char_idx]:
                matches += 1
            
            s2_count[char_idx] += 1
            
            start_char_idx = self.get_idx(s2[start])
            if s1_count[start_char_idx] == s2_count[start_char_idx]:
                matches -= 1
            elif s1_count[start_char_idx] == s2_count[start_char_idx] - 1:
                matches += 1
            
            s2_count[start_char_idx] -= 1
            start += 1
        
        return matches == 26


    def get_idx(self, char):
        return ord(char) - ord("a")