"""
URL of problem:
https://leetcode.com/problems/word-search-ii/
"""


from itertools import product


class Trie:
    def __init__(self):
        self.value = False
        self.children = {}


    def insert(self, word):
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Trie()

            current_node = current_node.children[char]

        current_node.value = True
        return


class Solution:
    def __init__(self):
        self.board = None
        self.num_rows = 0
        self.num_cols = 0
        self.visited = set()
        # West, North, East, South
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.words_trie = Trie()
        self.result = []


    def findWords(self, board, words):
        for word in words:
            self.words_trie.insert(word)

        self.board = board
        self.num_rows, self.num_cols = len(board), len(board[0])
        for row_idx, col_idx in product(range(self.num_rows), range(self.num_cols)):
            char = self.board[row_idx][col_idx]
            if char in self.words_trie.children:
                self.board[row_idx][col_idx] = "X"
                self.performDFS(row_idx, col_idx, [char], self.words_trie.children[char])
                self.board[row_idx][col_idx] = char

        return self.result


    def performDFS(self, row_idx, col_idx, path, curr_node):
        if curr_node.value:
            self.result.append(''.join(path))
            curr_node.value = False

        for row_diff, col_diff in self.directions:
            nbr_row, nbr_col = row_idx + row_diff, col_idx + col_diff
            within_bounds = 0 <= nbr_row < self.num_rows and 0 <= nbr_col < self.num_cols
            if within_bounds:
                nbr_char = self.board[nbr_row][nbr_col]
                if nbr_char in curr_node.children:
                    nbr_node = curr_node.children[nbr_char]
                    path.append(nbr_char)
                    self.board[nbr_row][nbr_col] = "X"
                    self.performDFS(nbr_row, nbr_col, path, nbr_node)
                    if not nbr_node.value and not nbr_node.children:
                        del curr_node.children[nbr_char]

                    self.board[nbr_row][nbr_col] = nbr_char
                    path.pop()

        return


def main():
    print(
        Solution().findWords(
            [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]],
            ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]
        )
    )


if __name__ == "__main__":
    main()
