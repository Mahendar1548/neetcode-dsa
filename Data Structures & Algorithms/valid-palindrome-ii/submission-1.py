class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return self._is_palindrome(s, start+1, end) or self._is_palindrome(s, start, end-1)
            start += 1
            end -= 1
        
        return True
    
    def _is_palindrome(self, s: str, start, end) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True