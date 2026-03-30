class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        max_len, start_idx, str_len = 1, 0, len(s)
        for i in range(str_len):
            temp_max, temp_start = self._is_find_max_palindrome(
                mid_idx=i, str_len=str_len, string_value=s)
            if temp_max > max_len:
                max_len, start_idx = temp_max, temp_start

        return s[start_idx: start_idx+max_len]

    def _is_find_max_palindrome(self, mid_idx, str_len, string_value):
        k = mid_idx - 1
        l = mid_idx + 1
        times = 0
        while k >= 0 and l < str_len:
            if string_value[k] != string_value[l]:
                break
            times += 1
            k -= 1
            l += 1
        max1, max1_start_idx = 2*times+1, mid_idx - times
        
        if mid_idx + 1 >= str_len or string_value[mid_idx] != string_value[mid_idx+1]:
            return max1, max1_start_idx
        print("why failing")
        k = mid_idx - 1
        l = mid_idx + 2
        times = 0
        while k >= 0 and l < str_len:
            if string_value[k] != string_value[l]:
                break
            times += 1
            k -= 1
            l += 1
        max2, max2_start_idx = 2*(times+1), mid_idx - times
        if max1 > max2:
            return max1, max1_start_idx
        else:
            return max2, max2_start_idx
        