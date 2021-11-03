"""
URL of problem:
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        unmatched_closing_bkts = 0
        stack_size = 0
        for char in s:
            if char == '(':
                stack_size += 1
            else:
                if not stack_size:
                    unmatched_closing_bkts += 1
                else:
                    stack_size -= 1

        return stack_size + unmatched_closing_bkts


    def minAddToMakeValid_2ndPass(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_unmatched_bkts, stack = 0, []
        for bracket in s:
            if bracket == '(':
                stack.append(bracket)
            else:
                if stack:
                    stack.pop()
                else:
                    num_unmatched_bkts += 1

        return num_unmatched_bkts + len(stack)


def main():
    print(Solution().minAddToMakeValid("()))(("))


if __name__ == "__main__":
    main()
