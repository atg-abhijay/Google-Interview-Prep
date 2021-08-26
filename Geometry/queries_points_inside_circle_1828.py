"""
URL of problem:
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""


class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        return []


def main():
    print(
        Solution().countPoints(
            [[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        )
    )


if __name__ == "__main__":
    main()
