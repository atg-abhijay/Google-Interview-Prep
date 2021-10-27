"""
URL of problem:
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""


import bisect


class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Time: O(mn), Space: O(1)
        # Tags: Geometry
        answer = [0] * len(queries)
        for idx, [centr_x, centr_y, radius] in enumerate(queries):
            boundary = radius ** 2
            for p_x, p_y in points:
                distance = (centr_x - p_x) ** 2 + (centr_y - p_y) ** 2
                if distance <= boundary:
                    answer[idx] += 1

        return answer


    def countPoints_2ndPass(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Time: O(mn), Space: O(1)
        # Tags: Geometry
        answer = []
        for center_x, center_y, radius in queries:
            num_inside = 0
            for x, y in points:
                if (center_x - x) ** 2 + (center_y - y) ** 2 <= radius ** 2:
                    num_inside += 1

            answer.append(num_inside)

        return answer


    def countPoints_sort_2ndPass(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        points.sort(key=lambda pt: pt[0])
        x_coords = [point[0] for point in points]
        for center_x, center_y, radius in queries:
            start_idx = bisect.bisect_left(x_coords, center_x-radius)
            # The index returned using bisect_right will be one AHEAD
            # of the last occurence of center_x + radius. Therefore,
            # we slice the list UP TO stop_idx so that the value
            # at stop_idx itself isn't considered in the loop.
            stop_idx = bisect.bisect_right(x_coords, center_x+radius)
            num_inside, boundary = 0, radius ** 2
            for x, y in points[start_idx:stop_idx]:
                if (center_x - x) ** 2 + (center_y - y) ** 2 <= boundary:
                    num_inside += 1

            answer.append(num_inside)

        return answer


def main():
    print(
        Solution().countPoints(
            [[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        )
    )


if __name__ == "__main__":
    main()
