"""
URL of problem:
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""


class Solution:
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        return False


def main():
    print(
        Solution().validPath(
            n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], start=0, end=5
        )
    )


if __name__ == "__main__":
    main()
