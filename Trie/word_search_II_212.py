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

        current_node.value = True
        return


    def search(self, word):
        current_node = self
        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.value


    def startsWith(self, prefix):
        current_node = self
        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return True


class Solution:
    def __init__(self):
        self.board = None
        self.num_rows = 0
        self.num_cols = 0
        self.visited = set()
        # West, North, East, South
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.words_trie = Trie()
        self.result = set()


    def findWords(self, board, words):
        for word in words:
            self.words_trie.insert(word)

        self.board = board
        self.num_rows, self.num_cols = len(board), len(board[0])
        for row_idx, col_idx in product(range(self.num_rows), range(self.num_cols)):
            char = self.board[row_idx][col_idx]
            if char in self.words_trie.children:
                self.visited.add((row_idx, col_idx))
                self.performDFS(row_idx, col_idx, [char], self.words_trie.children[char])
                self.visited.clear()

        return self.result


    def performDFS(self, row_idx, col_idx, path, curr_node):
        if curr_node.value:
            self.result.add(''.join(path))

        for row_diff, col_diff in self.directions:
            nbr_row, nbr_col = row_idx + row_diff, col_idx + col_diff
            within_bounds = 0 <= nbr_row < self.num_rows and 0 <= nbr_col < self.num_cols
            if within_bounds and (nbr_row, nbr_col) not in self.visited:
                nbr_char = self.board[nbr_row][nbr_col]
                if nbr_char in curr_node.children:
                    path.append(nbr_char)
                    self.visited.add((nbr_row, nbr_col))
                    self.performDFS(nbr_row, nbr_col, path, curr_node.children[nbr_char])
                    self.visited.remove((nbr_row, nbr_col))
                    path.pop()

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
