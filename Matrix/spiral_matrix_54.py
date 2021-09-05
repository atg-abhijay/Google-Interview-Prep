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


def main():
    print(Solution().spiralOrder([[1,2],[3,4]]))


if __name__ == "__main__":
    main()
