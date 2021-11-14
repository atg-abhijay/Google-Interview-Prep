"""
URL of problem:
https://leetcode.com/problems/climbing-stairs/
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1] * (n+1)
        for x in range(2, n+1):
            steps[x] = steps[x-1] + steps[x-2]

        return steps[n]


    def climbStairs_2ndPass(self, n):
        """
        :type n: int
        :rtype: int
        """
        return -1


def main():
    print(Solution().climbStairs(3))


if __name__ == "__main__":
    main()
