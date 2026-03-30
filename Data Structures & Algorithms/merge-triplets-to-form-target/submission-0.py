class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = None

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if ans is None:
                    ans = triplet

                ans = [max(ans[0], triplet[0]), max(ans[1], triplet[1]), max(ans[2], triplet[2])]
                if ans == target:
                    return True
        
        return False
