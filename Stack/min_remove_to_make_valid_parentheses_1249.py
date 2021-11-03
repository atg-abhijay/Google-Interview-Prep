"""
URL of problem:
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time: O(n), Space: O(n)
        # Tags: Stacks, Arrays
        s, opening_bkt_idxs, closing_bkt_idxs = list(s), [], []
        for idx, char in enumerate(s):
            if char == '(':
                opening_bkt_idxs.append(idx)
            elif char == ')':
                if opening_bkt_idxs:
                    opening_bkt_idxs.pop()
                else:
                    closing_bkt_idxs.append(idx)

        for idx in opening_bkt_idxs + closing_bkt_idxs:
            s[idx] = ""

        return ''.join(s)


def main():
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))


if __name__ == "__main__":
    main()
