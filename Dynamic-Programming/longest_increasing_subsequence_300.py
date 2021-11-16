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
        max_length, longest_so_far = 1, [1] * len(nums)
        for idx, num in enumerate(nums):
            rightmost_smaller_idx, greatest_ln = -1, 0
            for j, prev in enumerate(nums[:idx]):
                if prev < num and longest_so_far[j] > greatest_ln:
                    rightmost_smaller_idx = j
                    greatest_ln = longest_so_far[j]

#             if rightmost_smaller_idx == -1:
#                 continue

#             if nums[rightmost_smaller_idx] == num:
#                 longest_so_far[idx] = longest_so_far[rightmost_smaller_idx]
#             # else:
            if rightmost_smaller_idx != -1:
                longest_so_far[idx] = 1 + greatest_ln
            # if rightmost_smaller_idx == -1:
                # longest_so_far[idx] = 1
                # if idx - 1 >= 0:
                #     longest_so_far[idx] = longest_so_far[idx-1]


            max_length = max(max_length, longest_so_far[idx])

        return max_length


def main():
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == "__main__":
    main()
