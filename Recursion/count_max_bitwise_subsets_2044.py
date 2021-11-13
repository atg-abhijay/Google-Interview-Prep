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
        num_elems = len(nums)
        max_bitwise, num_subsets = 0, 0
        for combn in range(2 ** num_elems, 2 ** (num_elems + 1)):
            bitmask = bin(combn)[3:]
            subset = [num for bit, num in zip(bitmask, nums) if bit == '1']
            subset_OR = reduce(lambda x, y: x | y, subset, 0)
            if subset_OR > max_bitwise:
                max_bitwise = subset_OR
                num_subsets = 1
            elif subset_OR == max_bitwise:
                num_subsets += 1

        return num_subsets

def main():
    print(Solution().countMaxOrSubsets([2, 2, 2]))


if __name__ == "__main__":
    main()
