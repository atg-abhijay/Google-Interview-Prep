"""
URL of problem:
https://leetcode.com/problems/partition-equal-subset-sum/
"""


from collections import defaultdict


class Solution:
    def __init__(self):
        self.possible = defaultdict(lambda: defaultdict(bool))

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1 or len(nums) == 1:
            return False

        return self.partition(0, total_sum // 2, nums)

    def partition(self, idx, target, nums):
        if target < 0 or not nums[idx:]:
            self.possible[idx][target] = False
            return False

        if target == 0:
            self.possible[idx][target] = True
            return True

        if target not in self.possible[idx + 1]:
            if self.partition(idx + 1, target, nums):
                return True

        exclude_result = self.possible[idx + 1][target]

        sub_target = target - nums[idx]
        if sub_target not in self.possible[idx + 1]:
            if self.partition(idx + 1, sub_target, nums):
                return True

        include_result = self.possible[idx + 1][sub_target]
        return include_result or exclude_result


def main():
    print(Solution().canPartition([1, 5, 11, 5]))


if __name__ == "__main__":
    main()
