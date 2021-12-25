"""
URL of problem:
https://leetcode.com/problems/detonate-the-maximum-bombs/
"""


class Solution:
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        return 0


def main():
    print(
        Solution().maximumDetonation(
            [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
        )
    )


if __name__ == "__main__":
    main()
