"""
URL of problem:
https://leetcode.com/problems/possible-bipartition/
"""


from collections import deque


class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
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
    print(Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))


if __name__ == "__main__":
    main()
