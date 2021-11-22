"""
URL of problem:
https://leetcode.com/problems/word-search-ii/
"""


from itertools import product
from collections import defaultdict


class Trie:
    def __init__(self):
        self.value = False
        self.children = defaultdict(Trie)

    def insert(self, word):
        current_node = self
        for char in word:
            current_node = current_node.children[char]
            # Set all intermediate nodes to True as well
            current_node.value = True

        return

    def search(self, word):
        current_node = self
        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.value

class Solution:
    def __init__(self):
        self.board = None
        self.num_rows = 0
        self.num_cols = 0
        self.visited = set()
        # West, North, East, South
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.words_trie = Trie()


    def setUpData(self, board):
        self.board = board
        self.num_rows = len(board)
        self.num_cols = len(board[0])


    def findWords(self, board, words):
        self.setUpData(board)
        self.createWords()
        return [w for w in words if self.words_trie.search(w)]


    def createWords(self):
        for row_idx, col_idx in product(range(self.num_rows), range(self.num_cols)):
            self.visited.add((row_idx, col_idx))
            self.performDFS(row_idx, col_idx, [self.board[row_idx][col_idx]])
            self.visited.clear()

        return self.words_trie


    def performDFS(self, row_idx, col_idx, path):
        reached_dead_end = True
        for row_diff, col_diff in self.directions:
            nbr_row, nbr_col = row_idx + row_diff, col_idx + col_diff
            within_bounds = 0 <= nbr_row < self.num_rows and 0 <= nbr_col < self.num_cols
            if within_bounds and (nbr_row, nbr_col) not in self.visited:
                reached_dead_end = False
                path.append(self.board[nbr_row][nbr_col])
                self.visited.add((nbr_row, nbr_col))
                self.performDFS(nbr_row, nbr_col, path)
                self.visited.remove((nbr_row, nbr_col))
                path.pop()

        if reached_dead_end:
            self.words_trie.insert(''.join(path))

        return


def main():
    print(
        Solution().findWords(
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        )
    )


if __name__ == "__main__":
    main()
