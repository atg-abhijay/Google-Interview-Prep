"""
URL of problem:
https://leetcode.com/problems/longest-increasing-subsequence/
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        longest_so_far = [1] * len(nums)
        max_length = 0
        for idx, num in enumerate(nums):
            rightmost_smaller_idx = -1
            for j, prev in enumerate(nums[:idx]):
                if prev < num:
                    rightmost_smaller_idx = j

            if rightmost_smaller_idx == -1:
                if idx - 1 >= 0:
                    longest_so_far[idx] = longest_so_far[idx-1]
            else:
                longest_so_far[idx] = 1 + longest_so_far[rightmost_smaller_idx]

            max_length = max(max_length, longest_so_far[idx])

        return max_length


def main():
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == "__main__":
    main()
