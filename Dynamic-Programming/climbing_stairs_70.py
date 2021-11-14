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
        # Time: O(n), Space: O(n)
        # Tags: Dynamic Programming
        if n == 1:
            return 1

        ways = [1, 1]
        for _ in range(2, n+1):
            ways.append(ways[-1] + ways[-2])

        return ways[n]


def main():
    print(Solution().climbStairs(3))


if __name__ == "__main__":
    main()
