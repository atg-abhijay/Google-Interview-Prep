"""
URL of problem:
https://leetcode.com/problems/is-graph-bipartite/
"""


class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        return False


def main():
    print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))


if __name__ == "__main__":
    main()
