"""
URL of problem:
https://leetcode.com/problems/partition-equal-subset-sum/
"""


from itertools import product


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1 or len(nums) == 1:
            return False

        return self.partition(nums, total_sum // 2)

    def partition(self, nums, target):
        if target < 0 or not nums:
            return False

        if target == 0:
            return True

        exclude_result = self.partition(nums[1:], target)
        include_result = self.partition(nums[1:], target - nums[0])

        return include_result or exclude_result


def main():
    print(Solution().canPartition([1, 5, 11, 5]))


if __name__ == "__main__":
    main()
