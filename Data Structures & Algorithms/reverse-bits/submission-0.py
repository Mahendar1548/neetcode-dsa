class Solution:
    def reverseBits(self, n: int) -> int:
        data = list()
        for i in range(32):
            data.append(str(n & 1))
            n >>= 1
        
        return int("".join(data), 2)

        