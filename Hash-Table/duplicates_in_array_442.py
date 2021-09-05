"""
URL of problem:
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        result = []
        for num in nums[1:]:
            if nums[num] < 0:
                result.append(num)
            else:
                nums[num] *= (-1)

        return result


def main():
    print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == "__main__":
    main()
