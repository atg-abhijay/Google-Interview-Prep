"""
URL of problem:
https://leetcode.com/problems/set-matrix-zeroes/
"""


from itertools import product


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            if matrix[row_idx][col_idx] != 0:
                continue

            for idx, value in enumerate(matrix[row_idx]):
                if value != 0:
                    matrix[row_idx][idx] = 'A'

            for idx in range(num_rows):
                if matrix[idx][col_idx] != 0:
                    matrix[idx][col_idx] = 'A'

        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            if matrix[row_idx][col_idx] == 'A':
                matrix[row_idx][col_idx] = 0

        return


def main():
    print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))


if __name__ == "__main__":
    main()
