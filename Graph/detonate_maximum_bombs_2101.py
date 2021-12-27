"""
URL of problem:
https://leetcode.com/problems/detonate-the-maximum-bombs/
"""


from collections import defaultdict
from itertools import combinations


class Solution:
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        # Time:
        # - Graph creation: O(#bombs ^ 2)
        # - DFSes: O(#bombs * (#bombs + #edges))
        # - Total: O(#bombs * (#bombs + #edges))
        # Space: O(#bombs + #edges)
        # Tags: Graphs, DFS

        # Create an adjaceny list representation of
        # which bombs are in the radius of other bombs
        graph = defaultdict(set)
        for bomb_a, bomb_b in combinations(enumerate(bombs), 2):
            a_idx, [a_x_coord, a_y_coord, a_radius] = bomb_a
            b_idx, [b_x_coord, b_y_coord, b_radius] = bomb_b
            distance = (a_x_coord - b_x_coord) ** 2 + (a_y_coord - b_y_coord) ** 2
            if distance <= a_radius ** 2:
                graph[a_idx].add(b_idx)

            if distance <= b_radius ** 2:
                graph[b_idx].add(a_idx)

        # Start a fresh DFS from each bomb and check the number
        # of bombs that get detonated in the chain reaction
        max_detonations, visited = 0, set()
        for bomb in range(len(bombs)):
            visited.add(bomb)
            max_detonations = max(
                max_detonations, self.perform_dfs(graph, bomb, visited)
            )
            visited.clear()

        return max_detonations

    def perform_dfs(self, graph, bomb, visited):
        num_detonations = 1
        for nbr_bomb in graph[bomb]:
            if nbr_bomb not in visited:
                visited.add(nbr_bomb)
                num_detonations += self.perform_dfs(graph, nbr_bomb, visited)

        return num_detonations


def main():
    print(
        Solution().maximumDetonation(
            [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
        )
    )


if __name__ == "__main__":
    main()
