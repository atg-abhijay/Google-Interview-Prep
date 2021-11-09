"""
URL of problem:
https://leetcode.com/problems/course-schedule/
"""


from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        courses = set(x for x in range(numCourses))
        all_prereqs = dict((x, []) for x in courses)
        for target, pre_req in prerequisites:
            all_prereqs[target].append(pre_req)

        visited = [0 for _ in range(numCourses)]
        while courses:
            random_course = courses.pop()
            courses.add(random_course)
            queue = [random_course]
            while queue:
                cse = queue[-1]
                # First time exploring node
                if not visited[cse]:
                    visited[cse] = 1
                    for pre_req in all_prereqs[cse]:
                        if visited[pre_req] == 1:
                            return False

                        queue.append(pre_req)

                # Exploration in progress for node
                elif visited[cse] == 1:
                    if all(map(lambda x: visited[x] == 2, all_prereqs[cse])):
                        visited[cse] = 2
                        queue.pop()
                        courses.remove(cse)

                # Already explored node
                else:
                    queue.pop()

        return True


    def canFinish_2ndPass(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Time: O(#nodes + #edges), Space: O(#nodes + #edges)
        # Tags: Graphs, DFS

        if numCourses == 1 or not prerequisites:
            return True

        # Build an adjacency list representation of the graph
        courses = defaultdict(list)
        for crse, prereq in prerequisites:
            courses[crse].append(prereq)

        # 0 = not visited, 1 = in progress, 2 = completed
        visited = [0] * numCourses
        course_keys = set(courses.keys())
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
                        return False

                    visited[crse] = 2
                    stack.pop()

                else:
                    stack.pop()

        return True


def main():
    print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))


if __name__ == "__main__":
    main()
