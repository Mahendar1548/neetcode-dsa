class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        num_counter = Counter(nums)
        ans = []
        target_perm_len = len(nums)

        def backtrack(curr_len, current_comb):
            if curr_len == target_perm_len:
                ans.append(current_comb.copy())
                return

            for num in num_counter:
                if num_counter[num] > 0:
                    current_comb.append(num)
                    num_counter[num] -= 1
                    backtrack(curr_len+1, current_comb)
                    current_comb.pop()
                    num_counter[num] += 1
        
        backtrack(0, [])
        return ans