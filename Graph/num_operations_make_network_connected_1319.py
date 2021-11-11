"""
URL of problem:
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        return -1


def main():
    print(Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))


if __name__ == "__main__":
    main()
