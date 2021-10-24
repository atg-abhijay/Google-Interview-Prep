"""
URL of problem:
https://leetcode.com/problems/number-of-1-bits/
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_one_bits = 0
        while n > 0:
            num_one_bits += n & 1
            n >>= 1

        return num_one_bits


    def hammingWeight_2ndPass(self, num):
        """
        :type n: int
        :rtype: int
        """
        return -1


def main():
    print(Solution().hammingWeight(11))


if __name__ == "__main__":
    main()
