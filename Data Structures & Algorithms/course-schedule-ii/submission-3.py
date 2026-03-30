class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(set)
        for course, pre_req in prerequisites:
            pre_map[course].add(pre_req)

        cycle, visited = set(), set()
        order = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre_req_crs in list(pre_map[course]):
                if not dfs(pre_req_crs):
                    return False
    
            cycle.remove(course)
            visited.add(course)
            order.append(course)

            return True

        for i in range(numCourses):
            if not dfs(course=i):
                return []

        return order
