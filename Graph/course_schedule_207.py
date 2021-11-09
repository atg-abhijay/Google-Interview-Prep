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
        if numCourses == 1 or not prerequisites:
            return True

        courses = defaultdict(list)
        for crse, prereq in prerequisites:
            courses[crse].append(prereq)

        random_course = prerequisites[0][0]
        visited = set([random_course])
        queue = deque([random_course])
        while queue:
            crse = queue.popleft()
            for prereq in courses[crse]:
                if prereq in visited:
                    return False

                visited.add(prereq)
                queue.append(prereq)

        return True


def main():
    print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))


if __name__ == "__main__":
    main()
