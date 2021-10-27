"""
URL of problem:
https://leetcode.com/problems/mirror-reflection/
"""


class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # Half-working solution
        if p % q != 0:
            if p % q < q / 2:
                return 1
            if p % q > q / 2:
                return 2

            return 0

        if (p / q) % 2 == 0:
            return 2

        return 1


def main():
    print(Solution().mirrorReflection(4, 3))


if __name__ == "__main__":
    main()
