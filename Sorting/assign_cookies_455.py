"""
URL of problem:
https://leetcode.com/problems/assign-cookies/
"""


from bisect import bisect_left


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s:
            return 0

        content_children = 0
        g.sort(), s.sort()
        start_idx = 0
        for greed in g:
            size_idx = bisect_left(s, greed, lo=start_idx)
            if 0 <= size_idx < len(s):
                content_children += 1
                start_idx = size_idx + 1

        return content_children


def main():
    print(Solution().findContentChildren([10, 9, 8, 7], [3, 4, 5, 6]))


if __name__ == "__main__":
    main()
