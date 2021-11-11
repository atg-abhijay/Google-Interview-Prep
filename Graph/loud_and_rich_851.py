"""
URL of problem:
https://leetcode.com/problems/loud-and-rich/
"""


class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        return []


def main():
    print(
        Solution().loudAndRich(
            [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
            [3, 2, 5, 4, 6, 1, 7, 0],
        )
    )


if __name__ == "__main__":
    main()
