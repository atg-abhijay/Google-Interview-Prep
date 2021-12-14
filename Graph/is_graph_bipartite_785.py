"""
URL of problem:
https://leetcode.com/problems/is-graph-bipartite/
"""


from collections import deque


class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # Time: O(#nodes + #edges) - BFS runtime
        # Space: O(#nodes + #edges) - BFS space
        # Tags: Graphs, BFS
        partition = {}
        all_nodes = set(range(len(graph)))

        while all_nodes:
            queue = deque([all_nodes.pop()])
            partition[queue[0]] = 1
            while queue:
                node = queue.popleft()
                for nbr in graph[node]:
                    if nbr in partition and partition[node] == partition[nbr]:
                        return False

                    if nbr in all_nodes:
                        all_nodes.discard(nbr)
                        queue.append(nbr)
                        partition[nbr] = 1 - partition[node]

        return True


def main():
    print(Solution().isBipartite([[1, 4], [0, 2], [1], [4], [0, 3]]))


if __name__ == "__main__":
    main()
