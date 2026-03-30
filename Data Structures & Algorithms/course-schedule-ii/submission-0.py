class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        node_wise_dependents = defaultdict(set)
        node_wise_outgoing_count = {
            each: 0 for each in range(numCourses)
        }
        for a, b in prerequisites:
            node_wise_outgoing_count[a] += 1
            node_wise_dependents[b].add(a)

        order = []
        course_taken = 0
        while True:
            course_to_taken = None
            for course, count in node_wise_outgoing_count.items():
                if count == 0:
                    course_to_taken = course

            if course_to_taken is None:
                break
            order.append(course_to_taken)
            del node_wise_outgoing_count[course_to_taken]
            course_taken += 1
            dependent_courses = node_wise_dependents[course_to_taken]
            for each in dependent_courses:
                node_wise_outgoing_count[each] -= 1

        return order if course_taken == numCourses else []