"""
URL of problem:
https://leetcode.com/problems/word-search/
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        return False


def main():
    print(
        Solution().exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
        )
    )


if __name__ == "__main__":
    main()
