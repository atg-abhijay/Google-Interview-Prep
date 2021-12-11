"""
URL of problem:
https://leetcode.com/problems/combination-sum-iv/
"""


from collections import defaultdict, Counter
from functools import reduce
from math import factorial
from operator import mul


class Solution:
    def __init__(self):
        self.paths = defaultdict(set)

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        self.partition(0, target, nums)
        num_ways = 0
        for path in self.paths[(0, target)]:
            numtr = factorial(len(path))
            counter = Counter(path)
            demtr = reduce(mul, map(factorial, counter.values()))
            num_ways += numtr/demtr

        return int(num_ways)

    def partition(self, idx, target, nums):
        current_params = (idx, target)
        self.paths[current_params] = set()
        # Base cases
        if target == 0:
            self.paths[current_params].add(tuple())
            return

        if not nums[idx:] or target < nums[idx]:
            return

        # Exclude the number at idx
        exclusion_params = (idx + 1, target)
        if exclusion_params not in self.paths:
            self.partition(*exclusion_params, nums)

        self.paths[current_params].update(self.paths[exclusion_params])

        # Include the number at idx
        inclusion_params = (idx + 1, target - nums[idx])
        if inclusion_params not in self.paths:
            self.partition(*inclusion_params, nums)

        for sub_path in self.paths[inclusion_params]:
            self.paths[current_params].add(tuple([nums[idx]]) + sub_path)

        return


def main():
    print(Solution().combinationSum4([1, 2, 3], 4))


if __name__ == "__main__":
    main()
