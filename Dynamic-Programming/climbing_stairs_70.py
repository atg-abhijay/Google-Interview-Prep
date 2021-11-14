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
        # Time: O(n), Space: O(1)
        # Tags: Dynamic Programming
        if n == 1:
            return 1

        ways_two_before, ways_one_before = 1, 1
        ways_current = 0
        for _ in range(2, n+1):
            ways_current = ways_two_before + ways_one_before
            ways_two_before = ways_one_before
            ways_one_before = ways_current

        return ways_current


def main():
    print(Solution().climbStairs(3))


if __name__ == "__main__":
    main()
