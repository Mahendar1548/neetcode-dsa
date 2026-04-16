class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)

        if nums_sum % k != 0:
            return False

        partition_size = nums_sum // k
        partitions = [0 for i in range(k)]
        nums.sort(reverse=True)

        def backtrack(idx):
            if idx == len(nums):
                return True

            for i in range(k):
                if partitions[i] + nums[idx] <= partition_size:
                    partitions[i] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    partitions[i] -= nums[idx]
                if partitions[i] == 0:
                    break

            return False

        return backtrack(0)