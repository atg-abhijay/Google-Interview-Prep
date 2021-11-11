"""
URL of problem:
https://leetcode.com/problems/longest-consecutive-sequence/
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        min_val = min(nums)
        num_elems = len(nums)
        diffs = {x for x in range(num_elems)}
        for num in nums:
            diffs.discard(num - min_val)

        return num_elems - len(diffs)


def main():
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


if __name__ == "__main__":
    main()
