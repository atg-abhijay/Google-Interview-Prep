"""
URL of problem:
https://leetcode.com/problems/is-graph-bipartite/
"""


from collections import defaultdict, deque


class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        partition = defaultdict(int)
        all_nodes = set(range(len(graph)))

        which_set = 1
        while all_nodes:
            queue = deque([all_nodes.pop()])
            partition[queue[0]] = which_set
            which_set = 1 - which_set
            while queue:
                node = queue.popleft()
                for nbr in graph[node]:
                    if nbr in partition and partition[node] == partition[nbr]:
                        return False

                    if nbr in all_nodes:
                        all_nodes.discard(nbr)
                        queue.append(nbr)
                        partition[nbr] = which_set

                which_set = 1 - which_set

        return True


def main():
    print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))


if __name__ == "__main__":
    main()
