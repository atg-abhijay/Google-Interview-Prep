"""
URL of problem:
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
"""


from collections import defaultdict
import heapq


class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Build an adjacency list graph
        # representation of the input
        graph = defaultdict(dict)
        for u_node, v_node, time in roads:
            graph[u_node][v_node] = time
            # graph[v_node][u_node] = time

        min_times = {node: float('inf') for node in graph}
        min_times['s'] = 0
        heap, visited = [(0, 's')], set()
        while heap:
            _, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue

            visited.add(curr_node)

            for nbr, travel_time in graph[curr_node].items():
                if nbr in visited:
                    continue

                old_cost = min_times[nbr]
                new_cost = min_times[curr_node] + travel_time
                if new_cost < old_cost:
                    min_times[nbr] = new_cost
                    heapq.heappush(heap, (new_cost, nbr))

        return min_times


def main():
    print(
        Solution().countPaths(
            n=7,
            roads=[
                ['s', 't', 10],
                ['s', 'y', 5],
                ['t', 'y', 2],
                ['t', 'x', 2],
                ['y', 't', 1],
                ['y', 'x', 4],
                ['y', 'z', 6],
                ['x', 'z', 2],
                ['z', 'x', 7],
                ['z', 's', 3],
            ],
        )
    )


if __name__ == "__main__":
    main()
