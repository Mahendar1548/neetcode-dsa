class Solution:
    def countSubstrings(self, s: str) -> int:

        total_count, str_len = 0, len(s)
        for i in range(str_len):
            curr_count = self._is_find_max_palindrome(
                mid_idx=i, str_len=str_len, string_value=s)
            total_count += curr_count

        return total_count

    def _is_find_max_palindrome(self, mid_idx, str_len, string_value):
        curr_count = 1
        k = mid_idx - 1
        l = mid_idx + 1
        while k >= 0 and l < str_len:
            if string_value[k] != string_value[l]:
                break
            curr_count += 1
            k -= 1
            l += 1

        if mid_idx + 1 >= str_len or string_value[mid_idx] != string_value[mid_idx+1]:
            return curr_count
        curr_count += 1
        k = mid_idx - 1
        l = mid_idx + 2
        while k >= 0 and l < str_len:
            if string_value[k] != string_value[l]:
                break
            curr_count += 1
            k -= 1
            l += 1
        return curr_count
