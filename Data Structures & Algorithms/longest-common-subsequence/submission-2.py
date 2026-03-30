class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev_data = [0] * (len(text2) + 1)

        for i in range(len(text1)-1, -1, -1):
            curr_data = [0] * (len(text2) + 1)
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    curr_data[j] = 1 + (prev_data[j+1])
                else:
                    curr_data[j] = max(curr_data[j + 1], prev_data[j])
            prev_data = curr_data

        return prev_data[0]
