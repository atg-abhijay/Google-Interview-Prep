"""
URL of problem:
https://leetcode.com/problems/course-schedule-ii/
"""


from collections import defaultdict


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Time: O(#nodes + #edges), Space: O(#nodes + #edges)
        # Tags: Graphs, DFS
        if numCourses == 1 or not prerequisites:
            return list(range(numCourses))

        # Build an adjacency list representation of the graph
        courses = defaultdict(list)
        for crse, prereq in prerequisites:
            courses[crse].append(prereq)

        # 0 = not visited, 1 = in progress, 2 = completed
        visited = [0] * numCourses
        course_keys = set(range(numCourses))
        path = []
        # Build a solution based on DFSing into the prerequisites graph.
        # Two while loops to handle the case of a disconnected graph.
        # - If status of a course is 0, add it's prerequisites to the
        #   stack and change status to 1. Don't pop the course yet. We
        #   need to maintain the stack to build a path in the graph to
        #   be able to check for cycles.
        # - If status of a course is 1, check if all of it's prerequisites
        #   have been "completed" (status 2), meaning that they didn't
        #   yield any cycles. If that happens, change the status to 2 and
        #   pop the course. If all the prerequisites don't have status 2,
        #   that means that a cycle has been encountered and the courses
        #   cannot be finished.
        # - If status of a course is 2, it means that that course can be completed
        #   (it will not encounter any cycles). No need to traverse that course.
        while course_keys:
            stack = [course_keys.pop()]
            while stack:
                crse = stack[-1]
                course_keys.discard(crse)
                visit_status = visited[crse]

                if visit_status == 0:
                    stack.extend(courses[crse])
                    visited[crse] = 1

                elif visit_status == 1:
                    if not all(map(lambda pr: visited[pr] == 2, courses[crse])):
                        return []

                    visited[crse] = 2
                    path.append(stack.pop())

                else:
                    stack.pop()

        return path


def main():
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


if __name__ == "__main__":
    main()
