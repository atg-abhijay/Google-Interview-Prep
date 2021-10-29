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
        # Time: O(nm)(?), n for size of 'words'
        #       and m for average size of a word
        # Space: O(1), since there are 26 letters
        # Tags: Hash tables
        alphabets = {letter: idx for idx, letter in enumerate(order)}
        for f_word, s_word in zip(words, words[1:]):
            is_subset_word = True
            for f_char, s_char in zip(f_word, s_word):
                # First word comes before second word
                # - correct lexicographical order
                if alphabets[f_char] < alphabets[s_char]:
                    is_subset_word = False
                    break

                # First word comes after second word
                # - wrong lexicographical order
                if alphabets[f_char] > alphabets[s_char]:
                    return False

            # The words are same up till the end of the
            # shorter word. If first word is longer after
            # that - wrong lexicographical order
            if is_subset_word and len(f_word) > len(s_word):
                return False

        return True


def main():
    print(Solution().isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
