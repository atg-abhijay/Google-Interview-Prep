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
        num_rows, num_cols = len(grid), len(grid[0])
        ans = [-1] * num_cols
        for col_idx in range(num_cols):
            curr_row, curr_col = 0, col_idx
            while curr_row < num_rows:
                incline = grid[curr_row][curr_col]
                nbr_incline = 0
                if incline == 1 and curr_col + 1 < num_cols:
                    nbr_incline = grid[curr_row][curr_col + 1]

                if incline == -1 and curr_col - 1 >= 0:
                    nbr_incline = grid[curr_row][curr_col - 1]

                # If ball lands against the wall or
                # it gets stuck in a "V"-shaped pattern
                if nbr_incline == 0 or incline != nbr_incline:
                    ans[col_idx] = -1
                    break

                curr_row += 1
                curr_col += incline

            # If the ball falls out at the bottom
            if curr_row == num_rows:
                ans[col_idx] = curr_col

        return ans


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
