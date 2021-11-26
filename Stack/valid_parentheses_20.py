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
        # Time: O(n), Space: O(n)
        # Tags: Stacks, Hash tables
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


    def isValid_2ndPass(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        # Tags: Stacks, Hash tables
        pairs = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for bracket in s:
            if bracket in pairs.keys():
                stack.append(bracket)
            else:
                if not stack:
                    return False

                opening_bracket = stack.pop()
                if pairs[opening_bracket] != bracket:
                    return False

        if stack:
            return False

        return True


    def isValid_forTopicStrings_2ndPass(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'}': '{', ')': '(', ']': '['}
        stack = []
        for bkt in s:
            if bkt in brackets.values():
                stack.append(bkt)
            else:
                if not stack:
                    return False

                opening_bkt = stack.pop()
                if brackets[bkt] != opening_bkt:
                    return False

        # Unmatched opening brackets are left
        if stack:
            return False

        return True


def main():
    print(Solution().isValid("()[]{}"))


if __name__ == "__main__":
    main()
