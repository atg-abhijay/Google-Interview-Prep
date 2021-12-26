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



def main():
    print(
        Solution().maximumDetonation(
            [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
        )
    )


if __name__ == "__main__":
    main()
