"""
URL of problem:
https://leetcode.com/problems/maximal-network-rank/
"""


class Solution:
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        return 0


def main():
    print(
        Solution().maximalNetworkRank(
            8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        )
    )


if __name__ == "__main__":
    main()
