class Solution:

    def encode(self, strs: List[str]) -> str:
        data = []
        for s in strs:
            slen = len(s)
            data.append(f"{slen}#{s}")

        return "".join(data)

    def decode(self, s: str) -> List[str]:
        ans = []
        if not s:
            return ans

        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i+= 1
            slen = int(s[start:i])
            ans.append(s[i+1:i+1+slen])
            i = i + 1 + slen
            print(i, ans)

        return ans