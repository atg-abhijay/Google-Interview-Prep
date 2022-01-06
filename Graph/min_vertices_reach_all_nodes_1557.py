"""
URL of problem:
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
"""


class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        return []


def main():
    print(
        Solution().findSmallestSetOfVertices(
            n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
        )
    )


if __name__ == "__main__":
    main()
