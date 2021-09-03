"""
URL of problem:
https://leetcode.com/problems/valid-parentheses/
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {'}': '{', ')': '(', ']': '['}
        opening_bkts = matches.values()
        stack = []
        for char in s:
            if char in opening_bkts:
                stack.append(char)
            else:
                if not stack:
                    return False

                elem = stack.pop()
                if elem != matches[char]:
                    return False

        if stack:
            return False

        return True


def main():
    print(Solution().isValid("()[]{}"))


if __name__ == "__main__":
    main()
