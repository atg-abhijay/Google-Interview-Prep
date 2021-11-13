"""
URL of problem:
https://leetcode.com/problems/subsets-ii/
"""


from collections import defaultdict
from itertools import product


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        power_set = [[]]
        unique_nums = defaultdict(int)
        for num in nums:
            unique_nums[num] += 1

        for num, count in unique_nums.items():
            if count == 1:
                power_set.extend([p_set + [num] for p_set in power_set])
            else:
                sets = [[num] * x for x in range(1, count + 1)]
                power_set.extend([p + s for p, s in product(power_set, sets)])

        return power_set


def main():
    print(Solution().subsetsWithDup([10, 9, 9, 6, 6, 6]))


if __name__ == "__main__":
    main()
