"""
URL of problem:
https://leetcode.com/problems/find-center-of-star-graph/
"""


from collections import Counter
from itertools import chain

class Solution:
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        counter = Counter(chain(*edges[:2]))
        return counter.most_common(1)[0][0]


def main():
    print(Solution().findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))


if __name__ == "__main__":
    main()
