"""
URL of problem:
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""


from collections import defaultdict


class Solution:
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        # Build an adjancency list graph
        # representation from the edges
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        stack = [start]
        visited = set([start])
        while stack:
            node = stack.pop()
            if node == end:
                return True

            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    stack.append(nbr)

        return False


def main():
    print(
        Solution().validPath(
            n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], start=0, end=5
        )
    )


if __name__ == "__main__":
    main()
