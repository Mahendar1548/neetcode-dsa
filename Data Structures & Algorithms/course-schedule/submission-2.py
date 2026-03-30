class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(set)
        for course, pre_req in prerequisites:
            pre_map[course].add(pre_req)
            
        visited = set()
        
        def dfs(course):
            if not pre_map[course]:
                return True

            if course in visited:
                return False
            
            visited.add(course)
            
            for pre_req_crs in list(pre_map[course]):
                if dfs(pre_req_crs):
                    pre_map[course].remove(pre_req_crs)
            
            return True
                    
                
        
        for i in range(numCourses):
            if not dfs(course=i):
                return False
        
        return True