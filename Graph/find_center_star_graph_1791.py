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
        # Time: O(1), Space: O(1)
        # Tags: Graphs, Hash Tables
        counter = Counter(chain(*edges[:2]))
        return counter.most_common(1)[0][0]

    def findCenter_alternative(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # Time: O(1), Space: O(1)
        # Tags: Graphs, Hash Sets
        return set(edges[0]).intersection(set(edges[1])).pop()


def main():
    print(Solution().findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))


if __name__ == "__main__":
    main()
