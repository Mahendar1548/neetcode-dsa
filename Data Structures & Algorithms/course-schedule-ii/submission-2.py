class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(set)
        for course, pre_req in prerequisites:
            pre_map[course].add(pre_req)

        visited = set()
        order = []

        def dfs(course):
            if course in visited:
                return False

            visited.add(course)

            for pre_req_crs in list(pre_map[course]):
                if dfs(pre_req_crs):
                    pre_map[course].remove(pre_req_crs)
                else:
                    return False
            visited.remove(course)
            if course not in order:
                order.append(course)

            return True

        for i in range(numCourses):
            if not dfs(course=i):
                return []

        return order