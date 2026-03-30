class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        start = 0
        end = len(people) - 1
        people.sort()
        ans = 0
        while start <= end:
            if start == end:
                start += 1
            elif people[start] + people[end] <= limit:
                start += 1
                end -= 1
            elif people[start] + people[end] > limit:
                end -= 1
            ans += 1
        
        return ans