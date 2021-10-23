"""
URL of problem:
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The array is rotated n times, which is
        # equivalent to it not being rotated at all
        if nums[0] <= nums[-1]:
            return nums[0]

        start_idx, stop_idx = 0, len(nums) - 1
        while 1:
            mid_idx = (start_idx + stop_idx) // 2
            if nums[start_idx] < nums[mid_idx]:
                start_idx = mid_idx
            elif nums[start_idx] > nums[mid_idx]:
                stop_idx = mid_idx
            else:
                break

        return nums[stop_idx]


def main():
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))


if __name__ == "__main__":
    main()
