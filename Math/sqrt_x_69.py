"""
URL of problem:
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        lower, upper = 0, x
        while lower <= upper:
            middle = (lower + upper) / 2
            square = int(middle * middle)
            if square > x:
                upper = middle
            elif square < x:
                lower = middle
            else:
                break

        return int(middle)


def main():
    print(Solution().mySqrt(73))


if __name__ == "__main__":
    main()
