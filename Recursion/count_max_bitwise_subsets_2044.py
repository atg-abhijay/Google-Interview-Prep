"""
URL of problem:
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
"""


from functools import reduce


class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_bitwise, num_subsets = 0, 0
        power_set = [[]]
        for num in nums:
            power_set.extend([p_set + [num] for p_set in power_set])

        for p_set in power_set:
            p_set_OR = reduce(lambda x, y: x | y, p_set, 0)
            if p_set_OR > max_bitwise:
                max_bitwise = p_set_OR
                num_subsets = 1
            elif p_set_OR == max_bitwise:
                num_subsets += 1

        return num_subsets


def main():
    print(Solution().countMaxOrSubsets([2, 2, 2]))


if __name__ == "__main__":
    main()
