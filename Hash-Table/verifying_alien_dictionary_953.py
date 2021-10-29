"""
URL of problem:
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alphabets = {letter: idx for idx, letter in enumerate(order)}
        for f_word, s_word in zip(words, words[1:]):
            is_subset_word = True
            for f_char, s_char in zip(f_word, s_word):
                if alphabets[f_char] < alphabets[s_char]:
                    is_subset_word = False
                    break

                if alphabets[f_char] > alphabets[s_char]:
                    return False

            if is_subset_word and len(f_word) > len(s_word):
                return False

        return True


def main():
    print(Solution().isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
