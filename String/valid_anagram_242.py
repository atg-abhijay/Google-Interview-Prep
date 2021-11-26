"""
URL of problem:
https://leetcode.com/problems/valid-anagram/
"""


from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        # Tags: Strings, Hashmaps
        return Counter(s) == Counter(t)


def main():
    print(Solution().isAnagram(s="anagram", t="nagaram"))


if __name__ == "__main__":
    main()
