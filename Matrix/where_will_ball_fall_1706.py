"""
URL of problem:
https://leetcode.com/problems/where-will-the-ball-fall/
"""


class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        return []


def main():
    print(
        Solution().findBall(
            [
                [1, 1, 1, -1, -1],
                [1, 1, 1, -1, -1],
                [-1, -1, -1, 1, 1],
                [1, 1, 1, 1, -1],
                [-1, -1, -1, -1, -1],
            ]
        )
    )


if __name__ == "__main__":
    main()
