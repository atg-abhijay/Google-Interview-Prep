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
        # Base cases
        if target < 0 or not nums[idx:]:
            self.possible[idx][target] = False
            return False

        if target == 0:
            self.possible[idx][target] = True
            return True

        for tgt in [target, target - nums[idx]]:
            if tgt not in self.possible[idx + 1]:
                if self.partition(idx + 1, tgt, nums):
                    return True

        idx_routes = self.possible[idx + 1]
        return idx_routes[target] or idx_routes[target - nums[idx]]


def main():
    print(Solution().canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))


if __name__ == "__main__":
    main()
