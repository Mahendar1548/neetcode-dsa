class Solution:

    def encode(self, strs: List[str]) -> str:
        data = []
        for s in strs:
            slen = len(s)
            len_len = len(str(slen))
            data.append(f"{len_len}{slen}{s}")

        return "".join(data)

    def decode(self, s: str) -> List[str]:
        ans = []
        if not s:
            return ans
        
        i = 0
        while i < len(s):
            len_len = int(s[i])
            slen = int(s[i+1:i+1+len_len])
            ans.append(s[i+1+len_len:i+1+len_len+slen])
            i = i+1+len_len+slen
        
        return ans