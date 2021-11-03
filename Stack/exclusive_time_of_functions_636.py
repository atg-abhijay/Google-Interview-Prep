"""
URL of problem:
https://leetcode.com/problems/exclusive-time-of-functions/
"""


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        return []


def main():
    print(
        Solution().exclusiveTime(
            2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
        )
    )


if __name__ == "__main__":
    main()
