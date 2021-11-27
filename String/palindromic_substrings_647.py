"""
URL of problem:
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:
    def __init__(self):
        self.num_palinds = 0
        self.str_len = 0
        # self.palindromes = []

    def countSubstrings(self, s):
        self.str_len = len(s)
        for odd_len_idx in range(self.str_len):
            self.find_palinds(s, odd_len_idx, odd_len_idx)

        for even_len_idx in range(self.str_len - 1):
            self.find_palinds(s, even_len_idx, even_len_idx+1)

        # print(self.palindromes)
        return self.num_palinds


    def find_palinds(self, string, left_idx, right_idx):
        while left_idx >= 0 and right_idx < self.str_len:
            if string[left_idx] == string[right_idx]:
                self.num_palinds += 1
                # self.palindromes.append(string[left_idx:right_idx+1])
            else:
                break

            left_idx -= 1
            right_idx += 1


def main():
    print(Solution().countSubstrings("abba"))


if __name__ == "__main__":
    main()
