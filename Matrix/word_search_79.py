"""
URL of problem:
https://leetcode.com/problems/word-search/
"""


from itertools import product


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        num_rows, num_cols = len(board), len(board[0])
        range_rows, range_cols = range(num_rows), range(num_cols)
        if len(word) > num_rows * num_cols:
            return False

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[0 for _ in range_cols] for _ in range_rows]
        for row_idx, col_idx in product(range_rows, range_cols):
            if board[row_idx][col_idx] != word[0]:
                continue

            visited = [[0 for _ in range_cols] for _ in range_rows]
            indices = [row_idx, col_idx, 0]
            arrays = [board, visited, directions]
            if self.performDFS(indices, word, arrays):
                return True

        return False


    def performDFS(self, indices, word, arrays):
        row_idx, col_idx, word_idx = indices
        board, visited, directions = arrays
        if board[row_idx][col_idx] != word[word_idx]:
            return False

        if word_idx == len(word) - 1:
            return True

        visited[row_idx][col_idx] = 1
        is_found = False
        for incr_x, incr_y in directions:
            nbr_row, nbr_col = row_idx + incr_x, col_idx + incr_y
            if 0 <= nbr_row < len(board) and 0 <= nbr_col < len(board[0]):
                if visited[nbr_row][nbr_col]:
                    continue

                is_found |= self.performDFS([nbr_row, nbr_col, word_idx + 1], word, arrays)
                visited[nbr_row][nbr_col] = 0

        return is_found


def main():
    print(
        Solution().exist(
            [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
        )
    )


if __name__ == "__main__":
    main()
