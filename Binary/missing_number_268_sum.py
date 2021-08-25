"""
URL of problem:
https://leetcode.com/problems/missing-number/
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_values = len(nums)
        total_sum = int((num_values * (num_values + 1)) / 2)
        given_vals_sum = sum(nums)
        return total_sum - given_vals_sum


def main():
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    main()