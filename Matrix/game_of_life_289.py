"""
URL of problem:
https://leetcode.com/problems/game-of-life/
"""


from itertools import product


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Let M be the size of the input
        # Time: O(M), Space: O(1)
        # Tags: Matrices

        num_rows, num_cols = len(board), len(board[0])
        # Add an outer boundary to the board to
        # bypass conducting checks for corner cells
        for idx, row in enumerate(board):
            board[idx] = [0] + row + [0]

        board.insert(0, [0] * (num_cols+2))
        board.append([0] * (num_cols+2))

        # Since the states are 0/1, leverage binary numbers
        # to store the next state at the higher position and
        # the original state at the lower position
        for row_idx, col_idx in product(range(1, num_rows+1), range(1, num_cols+1)):
            cell_state = board[row_idx][col_idx]
            num_live_neighbours = self.calculateLiveNeighbours(row_idx, col_idx, board)
            next_state = 0
            if cell_state == 1 and num_live_neighbours in [2, 3]:
                next_state = 1

            elif cell_state == 0 and num_live_neighbours == 3:
                next_state = 1

            board[row_idx][col_idx] = (next_state << 1) | cell_state

        # Remove the previously introduced, outer boundary for the board
        board.pop()
        board.pop(0)
        for idx, row in enumerate(board):
            board[idx] = row[1:-1]

        # Update the board with the next states
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            board[row_idx][col_idx] >>= 1


    def calculateLiveNeighbours(self, row_idx, col_idx, board):
        directions = {
            "n": (-1, 0), "ne": (-1, 1), "e": (0, 1), "se": (1, 1),
            "s": (1, 0), "sw": (1, -1), "w": (0, -1), "nw": (-1, -1)
        }
        # The #live neighbours will be determined using the
        # original cell state. Therefore, extract the lowest bit
        num_live_neighbours = 0
        for row_diff, col_diff in directions.values():
            num_live_neighbours += board[row_idx + row_diff][col_idx + col_diff] & 1

        return num_live_neighbours


def main():
    print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))


if __name__ == "__main__":
    main()
