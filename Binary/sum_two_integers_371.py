"""
URL of problem:
https://leetcode.com/problems/sum-of-two-integers/
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Time: O(log n), Space: O(log n)
        # Tags: Binary
        og_a, og_b = a, b
        a, b = a & 1023, b & 1023
        carry, bits = 0, []
        while a or b:
            a_bit, b_bit = a & 1, b & 1
            bits_sum = carry ^ a_bit
            if not (carry & a_bit):
                carry = 0

            if bits_sum & b_bit:
                carry = 1

            bits_sum ^= b_bit
            bits.append(str(bits_sum))
            a, b = a >> 1, b >> 1

        bits.append(str(carry))
        sum_val = int("".join(reversed(bits)), 2)
        # If the sum is negative (the negative
        # sum won't show up as part of sum_val)
        if (og_a < 0 and abs(og_a) > abs(og_b)) or (og_b < 0 and abs(og_b) > abs(og_a)):
            return -1 * ((-1 * sum_val) % 1024)

        # If the sum is positive but
        # one of the numbers is negative
        if og_a < 0 or og_b < 0:
            return sum_val % 1024

        # If both numbers are positive
        return sum_val


def main():
    print(Solution().getSum(10, 12))


if __name__ == "__main__":
    main()
