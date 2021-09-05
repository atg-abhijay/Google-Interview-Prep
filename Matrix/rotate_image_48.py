"""
URL of problem:
https://leetcode.com/problems/rotate-image/
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        return


def main():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print("Original matrix:")
    for row in matrix:
        print(row)
    print()
    Solution().rotate(matrix)
    print("Rotated matrix:")
    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()
