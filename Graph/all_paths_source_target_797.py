"""
URL of problem:
https://leetcode.com/problems/all-paths-from-source-to-target/
"""


from collections import defaultdict


class Solution:
    def __init__(self):
        self.paths_from_node = defaultdict(list)
        self.target = -1

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.target = len(graph) - 1
        return self.find_paths_from_source(graph, 0)

    def find_paths_from_source(self, graph, source):
        if source in self.paths_from_node:
            return self.paths_from_node[source]

        if source == self.target:
            self.paths_from_node[source] = [[source]]
            return self.paths_from_node[source]

        for nbr in graph[source]:
            sub_paths = self.find_paths_from_source(graph, nbr)
            for sub_path in sub_paths:
                self.paths_from_node[source].append([source] + sub_path)

        return self.paths_from_node[source]


def main():
    print(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))


if __name__ == "__main__":
    main()
