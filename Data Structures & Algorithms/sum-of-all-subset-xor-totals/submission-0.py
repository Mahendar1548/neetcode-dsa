class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = [0]

        for num in nums:
            for i in range(len(ans)):
                ans.append(ans[i]^num)

        return sum(ans)