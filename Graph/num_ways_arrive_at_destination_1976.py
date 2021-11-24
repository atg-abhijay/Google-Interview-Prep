"""
URL of problem:
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
"""


class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        return -1


def main():
    print(
        Solution().countPaths(
            n=7,
            roads=[
                [0, 6, 7],
                [0, 1, 2],
                [1, 2, 3],
                [1, 3, 3],
                [6, 3, 3],
                [3, 5, 1],
                [6, 5, 1],
                [2, 5, 1],
                [0, 4, 5],
                [4, 6, 2],
            ],
        )
    )


if __name__ == "__main__":
    main()
