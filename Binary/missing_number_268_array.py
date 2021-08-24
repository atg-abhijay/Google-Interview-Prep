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
        all_nums = [0] * (len(nums)+1)
        for num in nums:
            all_nums[num] = 1

        for idx, num_found in enumerate(all_nums):
            if not num_found:
                return idx

def main():
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    main()
