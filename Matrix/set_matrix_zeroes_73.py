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


    def setZeroes_2ndPass(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        change_rows, change_cols = [0] * num_rows, [0] * num_cols
        for row_idx, row in enumerate(matrix):
            for col_idx, elem in enumerate(row):
                if elem == 0:
                    change_rows[row_idx] = 1
                    change_cols[col_idx] = 1

        for idx, flag in enumerate(change_rows):
            if flag:
                matrix[idx] = [0] * num_cols

        for idx, flag in enumerate(change_cols):
            if not flag:
                continue

            for row in matrix:
                row[idx] = 0

        return


def main():
    print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))


if __name__ == "__main__":
    main()
