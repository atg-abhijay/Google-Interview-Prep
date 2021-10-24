"""
URL of problem:
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # Time: O(1), Space: O(1)
        # Tags: Binary
        result = 0
        for _ in range(32):
            result |= (n & 1)
            result <<= 1
            n >>= 1

        return result >> 1


    def reverseBits_2ndPass(self, n: int) -> int:
        # Time: O(1), Space: O(1)
        # Tags: Binary
        rev_num = 0
        for _ in range(32):
            rev_num |= n & 1
            rev_num <<= 1
            n >>= 1

        return rev_num >> 1


def main():
    print(Solution().reverseBits(4294967293))


if __name__ == "__main__":
    main()
