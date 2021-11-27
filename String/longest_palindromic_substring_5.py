"""
URL of problem:
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def __init__(self):
        self.longest_palind = None
        self.longest_len = 0
        self.str_len = 0
        # self.palindromes = []

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.str_len = len(s)
        for idx in range(self.str_len):
            # 1. Will find odd length palindromes
            # 2. Will find even length palindromes
            self.find_palind(s, idx, idx)
            self.find_palind(s, idx, idx+1)

        # print(self.palindromes)
        return self.longest_palind


    def find_palind(self, string, left_idx, right_idx):
        while left_idx >= 0 and right_idx < self.str_len:
            if string[left_idx] == string[right_idx]:
                # self.num_palinds += 1
                if right_idx - left_idx + 1 > self.longest_len:
                    self.longest_len = right_idx - left_idx + 1
                    self.longest_palind = string[left_idx:right_idx+1]
                # self.palindromes.append(string[left_idx:right_idx+1])
            else:
                break

            left_idx -= 1
            right_idx += 1


def main():
    print(Solution().longestPalindrome("cbbd"))


if __name__ == "__main__":
    main()
