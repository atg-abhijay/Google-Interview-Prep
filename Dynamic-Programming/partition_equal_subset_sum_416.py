"""
URL of problem:
https://leetcode.com/problems/partition-equal-subset-sum/
"""


from math import ceil


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1 or len(nums) == 1:
            return False

        nums.sort()
        target, curr_sum = total_sum // 2, 0
        start_idx, stop_idx = 0, len(nums) - 1
        while start_idx < stop_idx:
            mid_idx = ceil((start_idx + stop_idx)/2)
            curr_sum += sum(nums[start_idx:mid_idx])
            if curr_sum < target:
                start_idx = mid_idx
            elif curr_sum == target:
                return True
            else:
                return False

        return False


def main():
    print(Solution().canPartition([1, 2, 3, 5]))


if __name__ == "__main__":
    main()
