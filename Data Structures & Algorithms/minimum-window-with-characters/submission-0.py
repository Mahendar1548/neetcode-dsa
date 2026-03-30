class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = defaultdict(int)
        win_counter = defaultdict(int)

        for i in range(len(t)):
            t_counter[t[i]] += 1
            if i != len(t) - 1:
                win_counter[s[i]] += 1

        left = 0
        min_len = float('inf')
        ans_start = -1

        for i in range(len(t)-1, len(s)):
            win_counter[s[i]] += 1
            print(left,i, dict(t_counter), dict(win_counter))
            while self._compare_first_with_second(t_counter, win_counter):
                if min_len > i-left + 1:
                    min_len = i - left + 1
                    ans_start = left
                win_counter[s[left]] -= 1
                left += 1
        
        return s[ans_start: ans_start + min_len] if ans_start != -1 else ""

    def _compare_first_with_second(self, dict1, dict2):
        for key in dict1:
            if dict1[key] > dict2[key]:
                return False

        return True
