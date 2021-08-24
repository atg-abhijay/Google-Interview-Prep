"""
URL of problem:
https://leetcode.com/problems/house-robber/
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0, 0] + nums
        num_elems = len(nums)
        max_profits = [0] * (num_elems)
        for idx in range(2, num_elems):
            max_profits[idx] = max(
                max_profits[idx - 1], nums[idx] + max_profits[idx - 2]
            )

        return max_profits[-1]


def main():
    print(Solution().rob([2, 7, 9, 3, 1]))


if __name__ == "__main__":
    main()
