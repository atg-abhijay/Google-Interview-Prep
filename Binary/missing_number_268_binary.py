"""
URL of problem:
https://leetcode.com/problems/missing-number/
"""


from functools import reduce


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Alternate solution:
        # return reduce(
        #     lambda xor, tup: xor ^ tup[0] ^ tup[1], enumerate(nums), len(nums)
        # )
        xor_value = len(nums)
        for idx, num in enumerate(nums):
            xor_value ^= idx ^ num

        return xor_value


    def missingNumber_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return -1


def main():
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    main()
