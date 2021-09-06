"""
URL of problem:
https://leetcode.com/problems/unique-paths/
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (1, 0)]
        return self.performDFS([grid, directions], [0, 0], [m, n])


    def performDFS(self, arrays, indices, constants):
        grid, directions = arrays
        row_idx, col_idx = indices
        num_rows, num_cols = constants
        if grid[row_idx][col_idx] == 1:
            return 0

        if row_idx == num_rows-1 and col_idx == num_cols-1:
            return 1

        num_paths = 0
        grid[row_idx][col_idx] = 1
        for incr_x, incr_y in directions:
            nbr_row, nbr_col = row_idx + incr_x, col_idx + incr_y
            if 0 <= nbr_row < len(grid) and 0 <= nbr_col < len(grid[0]):
                num_paths += self.performDFS(arrays, [nbr_row, nbr_col], constants)
                grid[nbr_row][nbr_col] = 0

        return num_paths


def main():
    print(Solution().uniquePaths(3, 7))


if __name__ == "__main__":
    main()
