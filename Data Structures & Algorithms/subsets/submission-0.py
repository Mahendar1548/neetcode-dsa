class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def generate(data, start):
            ans.append(list(data))

            for i in range(start, len(nums)):
                generate(data + [nums[i]], i + 1)

        generate([], 0)
        return ans