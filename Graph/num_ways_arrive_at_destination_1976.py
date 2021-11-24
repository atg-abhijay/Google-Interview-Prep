"""
URL of problem:
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
"""


from collections import defaultdict
import heapq


class Solution:
    def __init__(self):
        self.graph = None
        self.visited = set()
        self.shortest_time = 0
        self.target = -1
        self.num_ways = 0

    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Build an adjacency list graph
        # representation of the input
        self.graph = defaultdict(dict)
        for u_node, v_node, time in roads:
            self.graph[u_node][v_node] = time
            self.graph[v_node][u_node] = time

        self.target = n - 1
        self.determineShortestPath(n)
        self.visited.add(0)
        self.performDFS(0, 0, [0])
        return self.num_ways

    def performDFS(self, curr_node, path_time, path):
        if curr_node == self.target:
            self.num_ways += 1
            print(path)
            return

        for nbr, travel_time in self.graph[curr_node].items():
            new_time = path_time + travel_time
            if nbr not in self.visited and new_time <= self.shortest_time:
                self.visited.add(nbr)
                path.append(nbr)
                self.performDFS(nbr, new_time, path)
                path.pop()
                self.visited.remove(nbr)

        return

    def determineShortestPath(self, n):
        # Use Dijkstra's algorithm
        min_times = {node: float("inf") for node in range(n)}
        min_times[0] = 0
        heap, visited = [(0, 0)], set()
        while heap:
            _, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue

            visited.add(curr_node)
            for nbr, travel_time in self.graph[curr_node].items():
                if nbr in visited:
                    continue

                old_cost = min_times[nbr]
                new_cost = min_times[curr_node] + travel_time
                if new_cost < old_cost:
                    min_times[nbr] = new_cost
                    heapq.heappush(heap, (new_cost, nbr))

        self.shortest_time = min_times[n - 1]


def main():
    print(
        Solution().countPaths(
            n=7,
            roads=[
                [0, 6, 7],
                [0, 1, 2],
                [1, 2, 3],
                [1, 3, 3],
                [6, 3, 3],
                [3, 5, 1],
                [6, 5, 1],
                [2, 5, 1],
                [0, 4, 5],
                [4, 6, 2],
            ],
        )
    )


if __name__ == "__main__":
    main()
