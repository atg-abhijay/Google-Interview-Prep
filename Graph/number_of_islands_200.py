"""
URL of problem:
https://leetcode.com/problems/number-of-islands/
"""


from collections import deque
from itertools import product


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            if grid[row_idx][col_idx] != "1":
                continue

            # A piece of land that hasn't been explored yet. Change the
            # value - the higher 1 denotes that the cell is part of an
            # island and the lower 1 that the cell contains land
            grid[row_idx][col_idx] = (1 << 1) | 1
            num_islands += 1
            queue = deque([(row_idx, col_idx)])
            while queue:
                row, col = queue.popleft()
                for row_diff, col_diff in directions:
                    nbr_row, nbr_col = row + row_diff, col + col_diff
                    within_bounds = 0 <= nbr_row < num_rows and 0 <= nbr_col < num_cols
                    if within_bounds and grid[nbr_row][nbr_col] == "1":
                        queue.append([nbr_row, nbr_col])
                        grid[nbr_row][nbr_col] = (1 << 1) & 1

        return num_islands


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
