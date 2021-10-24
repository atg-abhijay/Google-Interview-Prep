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
        # Time: O(log n), Space: O(1)
        # Tags: Binary
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
        # Time: O(#set bits), Space: O(1)
        # Tags: Binary

        # Method learnt from bitCount() method
        # on https://wiki.python.org/moin/BitManipulation
        num_one_bits = 0
        while num > 0:
            num &= num - 1
            num_one_bits += 1

        return num_one_bits


def main():
    print(Solution().hammingWeight(0b00000000000000000000000000001011))


if __name__ == "__main__":
    main()
