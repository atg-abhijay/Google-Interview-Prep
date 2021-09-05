"""
URL of problem:
https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], idx]

            dictionary[num] = idx


def main():
    print(Solution().twoSum([3, 2, 4], 6))


if __name__ == "__main__":
    main()
