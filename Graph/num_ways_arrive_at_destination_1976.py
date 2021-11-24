"""
URL of problem:
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
"""


from collections import defaultdict
import heapq


class Solution:
    def __init__(self):
        self.graph = defaultdict(dict)
        self.visited = set()
        self.shortest_time = 0
        self.num_ways = 0
        self.min_times = {}
        self.ways_from_nodes = defaultdict(lambda: defaultdict(int))

    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if not roads:
            return 1

        # Build an adjacency list graph
        # representation of the input
        for u_node, v_node, time in roads:
            self.graph[u_node][v_node] = time
            self.graph[v_node][u_node] = time

        self.determineShortestPath(n)
        self.visited.add(n-1)
        result = self.performDFS(n-1, self.shortest_time)
        return result

    def performDFS(self, curr_node, journey_money):
        if curr_node == 0:
            self.ways_from_nodes[curr_node][journey_money] += 1
            return

        for nbr, edge_cost in self.graph[curr_node].items():
            money_left = journey_money - edge_cost
            not_visited = nbr not in self.visited
            money_check = money_left >= self.min_times[nbr]
            did_compute_before = money_left in self.ways_from_nodes[nbr]
            if not_visited and money_check and not did_compute_before:
                self.visited.add(nbr)
                self.performDFS(nbr, money_left)
                self.visited.remove(nbr)

            if money_check:
                self.ways_from_nodes[curr_node][journey_money] += self.ways_from_nodes[nbr][money_left]

        return self.ways_from_nodes[curr_node][journey_money] % (10 ** 9 + 7)

    def determineShortestPath(self, n):
        # Use Dijkstra's algorithm
        self.min_times = {node: float("inf") for node in range(n)}
        self.min_times[0] = 0
        heap, visited = [(0, 0)], set()
        while heap:
            _, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue

            visited.add(curr_node)
            for nbr, travel_time in self.graph[curr_node].items():
                if nbr in visited:
                    continue

                old_cost = self.min_times[nbr]
                new_cost = self.min_times[curr_node] + travel_time
                if new_cost < old_cost:
                    self.min_times[nbr] = new_cost
                    heapq.heappush(heap, (new_cost, nbr))

        self.shortest_time = self.min_times[n-1]


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
