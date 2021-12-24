"""
URL of problem:
https://leetcode.com/problems/maximal-network-rank/
"""


from collections import defaultdict
from itertools import combinations


class Solution:
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Time: O(n^2), Space: O(#cities + #roads)
        # Tags: Graphs
        graph = defaultdict(set)
        for city_a, city_b in roads:
            graph[city_a].add(city_b)
            graph[city_b].add(city_a)

        max_network_rank = 0
        for city_a, city_b in combinations(range(n), 2):
            pair_rank = len(graph[city_a]) + len(graph[city_b])
            if city_a in graph[city_b]:
                pair_rank -= 1

            max_network_rank = max(max_network_rank, pair_rank)

        return max_network_rank


def main():
    print(
        Solution().maximalNetworkRank(
            8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        )
    )


if __name__ == "__main__":
    main()
