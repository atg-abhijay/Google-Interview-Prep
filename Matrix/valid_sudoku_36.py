"""
URL of problem:
https://leetcode.com/problems/valid-sudoku/
"""


from itertools import product


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        unique_nums = set()
        # Check the rows
        for row in board:
            for number in row:
                if number in unique_nums:
                    return False

                if number != '.':
                    unique_nums.add(number)

            unique_nums.clear()

        # Check the columns
        for col_idx in range(9):
            for row_idx in range(9):
                number = board[row_idx][col_idx]
                if number in unique_nums:
                    return False

                if number != '.':
                    unique_nums.add(number)

            unique_nums.clear()

        # Check the sub-boxes
        for box_row, box_col in product([0, 3, 6], [0, 3, 6]):
            for row_idx, col_idx in product(range(box_row, box_row + 3), range(box_col, box_col + 3)):
                number = board[row_idx][col_idx]
                if number in unique_nums:
                    return False

                if number != '.':
                    unique_nums.add(number)

            unique_nums.clear()

        return True


def main():
    print(
        Solution().isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )


if __name__ == "__main__":
    main()
