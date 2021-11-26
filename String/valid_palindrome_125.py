"""
URL of problem:
https://leetcode.com/problems/valid-palindrome/
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanum_str = ''.join(filter(lambda x: x.isalnum(), s)).lower()
        for char, rev_char in zip(alphanum_str, reversed(alphanum_str)):
            if char != rev_char:
                return False

        return True


def main():
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
    main()
