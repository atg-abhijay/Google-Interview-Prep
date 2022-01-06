"""
URL of problem:
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
"""


from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        all_vertices = set(range(n))
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)

        for vertex in range(n):
            if vertex not in all_vertices:
                continue

            stack = [vertex]
            first_itn = True
            while stack:
                vertex = stack.pop()
                if not first_itn:
                    all_vertices.discard(vertex)

                for nbr in graph[vertex]:
                    if nbr in all_vertices:
                        all_vertices.discard(nbr)
                        stack.append(nbr)

                first_itn = False

        return all_vertices


def main():
    print(
        Solution().findSmallestSetOfVertices(
            n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
        )
    )


if __name__ == "__main__":
    main()
