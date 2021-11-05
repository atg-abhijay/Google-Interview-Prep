"""
URL of problem:
https://leetcode.com/problems/spiral-matrix/
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_start, col_start = 0, 0
        row_end, col_end = len(matrix)-1, len(matrix[0])-1
        spiral_order = []

        while row_start <= row_end and col_start <= col_end:
            for idx in range(col_start, col_end+1):
                spiral_order.append(matrix[row_start][idx])

            row_start += 1
            for idx in range(row_start, row_end+1):
                spiral_order.append(matrix[idx][col_end])

            col_end -= 1
            if row_start > row_end or col_end < col_start:
                break

            for idx in range(col_end, col_start-1, -1):
                spiral_order.append(matrix[row_end][idx])

            row_end -= 1
            for idx in range(row_end, row_start-1, -1):
                spiral_order.append(matrix[idx][col_start])

            col_start += 1

        return spiral_order


    def spiralOrder_2ndPass(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not any(matrix):
            return []

        num_rows, num_cols = len(matrix), len(matrix[0])
        if num_rows == 1:
            return matrix[0]

        if num_cols == 1:
            return [row[0] for row in matrix]

        row_start, row_end = 0, num_rows - 1
        col_start, col_end = 0, num_cols - 1

        top_row = matrix[0][col_start:col_end]
        bottom_row = matrix[row_end][col_end:col_start:-1]
        right_col = [row[col_end] for row in matrix[row_start:row_end]]
        left_col = [row[col_start] for row in matrix[row_end:row_start:-1]]

        spiral_list = [*top_row, *right_col, *bottom_row, *left_col]
        matrix = [row[col_start+1:col_end] for row in matrix[row_start+1:row_end]]
        spiral_list.extend(self.spiralOrder_2ndPass(matrix))

        return spiral_list


def main():
    print(
        Solution().spiralOrder_2ndPass(
            [
                [1, 11],
                [2, 12],
                [3, 13],
                [4, 14],
                [5, 15],
                [6, 16],
                [7, 17],
                [8, 18],
                [9, 19],
                [10, 20],
            ]
        )
    )


if __name__ == "__main__":
    main()
