"""
URL of problem:
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time: O(log n), Space: O(1)
        # Tags: Arrays, Binary Search

        # Add a dummy value at the end to be able
        # to return the last index if that is the answer
        nums.append(float('inf'))
        start_idx, stop_idx = 0, len(nums) - 1
        while 1:
            mid_idx = (start_idx + stop_idx) // 2
            start_val, mid_val = nums[start_idx], nums[mid_idx]
            if start_val < mid_val:
                if start_val <= target < mid_val:
                    stop_idx = mid_idx
                else:
                    start_idx = mid_idx

            elif start_val > mid_val:
                if target >= start_val or target < mid_val:
                    stop_idx = mid_idx
                else:
                    start_idx = mid_idx

            else:
                return start_idx if target == start_val else -1


def main():
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))


if __name__ == "__main__":
    main()
