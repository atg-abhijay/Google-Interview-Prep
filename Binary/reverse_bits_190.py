"""
URL of problem:
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result |= (n & 1)
            result <<= 1
            n >>= 1

        return result >> 1


def main():
    print(Solution().reverseBits(4294967293))


if __name__ == "__main__":
    main()
