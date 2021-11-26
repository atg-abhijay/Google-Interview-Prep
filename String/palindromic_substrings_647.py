"""
URL of problem:
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:
    def __init__(self):
        self.num_palinds = 0
        self.palindromes = []
        self.str_len = 0
        self.visited = set()

    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        self.str_len = len(s)
        self.palindromes.extend([char for char in s])
        self.num_palinds += self.str_len

        self.checkIdx(s, 0, self.str_len - 1)
        print(self.palindromes)
        return self.num_palinds

    def checkIdx(self, string, start_idx, stop_idx):
        if start_idx == stop_idx:
            return

        mid_idx = (start_idx + stop_idx) // 2
        left_idx, right_idx = mid_idx - 1, mid_idx + 1
        while left_idx >= 0 and right_idx <= self.str_len - 1:
            if string[left_idx] == string[right_idx]:
                self.num_palinds += 1
                self.palindromes.append(string[left_idx:right_idx+1])
                left_idx -= 1
                right_idx += 1
            else:
                left_idxs, right_idxs = (start_idx, mid_idx), (mid_idx + 1, stop_idx)
                if left_idxs not in self.visited:
                    self.visited.add(left_idxs)
                    self.checkIdx(string, *left_idxs)
                if right_idxs not in self.visited:
                    self.visited.add(right_idxs)
                    self.checkIdx(string, *right_idxs)
                break

        return


def main():
    print(Solution().countSubstrings("racecarbob"))


if __name__ == "__main__":
    main()
