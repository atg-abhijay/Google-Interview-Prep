"""
URL of problem:
https://leetcode.com/problems/possible-bipartition/
"""


class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        return False


def main():
    print(Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))


if __name__ == "__main__":
    main()
