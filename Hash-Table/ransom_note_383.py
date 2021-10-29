"""
URL of problem:
https://leetcode.com/problems/ransom-note/
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        # Tags: Hash tables
        rsm_letters, mzn_letters = dict(), dict()
        for string, dictionary in [[ransomNote, rsm_letters], [magazine, mzn_letters]]:
            for letter in string:
                if letter not in dictionary:
                    dictionary[letter] = 1
                else:
                    dictionary[letter] += 1

        for letter, count in rsm_letters.items():
            if letter not in mzn_letters:
                return False

            if count > mzn_letters[letter]:
                return False

        return True


    def canConstruct_2ndPass(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        # Tags: Hash tables
        letter_counts = {}
        for char in magazine:
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] += 1

        for char in ransomNote:
            if char not in letter_counts:
                return False

            if letter_counts[char] == 0:
                return False

            letter_counts[char] -= 1

        return True


def main():
    print(Solution().canConstruct("aa", "aab"))


if __name__ == "__main__":
    main()
