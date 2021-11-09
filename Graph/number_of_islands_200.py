"""
URL of problem:
https://leetcode.com/problems/number-of-islands/
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return -1


def main():
    print(
        Solution().numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )


if __name__ == "__main__":
    main()
