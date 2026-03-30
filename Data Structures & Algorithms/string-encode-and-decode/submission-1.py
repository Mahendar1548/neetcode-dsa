class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str_val in strs:
            encoded_str += str(len(str_val)) + str_val
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while i < len(s):
            ans.append(s[i+1: int(s[i])+i+1])
            i += 1+int(s[i])
        return ans
