"""
URL of problem:
https://leetcode.com/problems/course-schedule/
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        return False


def main():
    print(Solution().canFinish(2, [[1, 0]]))


if __name__ == "__main__":
    main()
