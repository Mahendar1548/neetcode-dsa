class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [(i, j) for i, j in zip(capital, profits)]
        pairs.sort()

        max_heap = []
        curr_projects = 0
        i = 0
        
        while curr_projects < k:
            while i < len(pairs) and pairs[i][0] <= w:
                heapq.heappush(max_heap, -pairs[i][1])
                i += 1
            
            if not max_heap:
                break
            w += -1 * heapq.heappop(max_heap)
            curr_projects += 1

        return w