class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_wise_dependents = defaultdict(set)
        node_wise_outgoing_count = {
            each: 0 for each in range(numCourses)
        }
        for a, b in prerequisites:
            node_wise_outgoing_count[a] += 1
            node_wise_dependents[b].add(a)

        course_taken = 0
        while True:
            course_to_taken = None
            for course, count in node_wise_outgoing_count.items():
                if count == 0:
                    course_to_taken = course

            if course_to_taken is None:
                break

            del node_wise_outgoing_count[course_to_taken]
            course_taken += 1
            dependent_courses = node_wise_dependents[course]
            for each in dependent_courses:
                node_wise_outgoing_count[each] -= 1

        return course_taken == numCourses