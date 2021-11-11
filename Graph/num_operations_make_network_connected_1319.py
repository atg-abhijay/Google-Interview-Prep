"""
URL of problem:
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""


from collections import defaultdict, deque


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # Build an adjacency list representation
        # of the graph of connections in the network
        graph = defaultdict(list)
        for node_a, node_b in connections:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        num_conns = len(connections)
        computers, num_bfs_edges = set(range(n)), 0
        visited, num_discontd_networks = set(), 0
        while computers:
            queue = deque([computers.pop()])
            visited.add(queue[0])
            num_discontd_networks += 1
            while queue:
                computer = queue.popleft()
                computers.discard(computer)
                for nbr in graph[computer]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)
                        num_bfs_edges += 1

        if num_conns - num_bfs_edges >= num_discontd_networks - 1:
            return num_discontd_networks - 1

        return -1


def main():
    print(Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))


if __name__ == "__main__":
    main()
