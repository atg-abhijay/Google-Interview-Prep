"""
URL of problem:
https://leetcode.com/problems/maximum-subarray/
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        sums_so_far = [nums[0]]
        for idx, num in enumerate(nums[1:]):
            sums_so_far.append(max(num, num + sums_so_far[idx]))
            max_sum = max(max_sum, sums_so_far[-1])

        return max_sum


    def maxSubArray_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            current_sum = max(num, num + current_sum)
            max_sum = max(max_sum, current_sum)

        return max_sum


def main():
    print(Solution().maxSubArray([-2, -1, -3, -4, -1, -2, -1, -5, -4]))


if __name__ == "__main__":
    main()
