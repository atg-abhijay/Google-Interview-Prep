"""
URL of problem:
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # Time: O(n), Space: O(1)
        # Tags: Geometry
        slope_dmtr = (coordinates[1][0] - coordinates[0][0])
        if slope_dmtr == 0:
            slope = float('inf')
        else:
            slope = (coordinates[1][1] - coordinates[0][1]) / slope_dmtr

        for point, next_point in zip(coordinates[1:], coordinates[2:]):
            slope_dmtr = (next_point[0] - point[0])
            if slope_dmtr == 0:
                points_slope = float('inf')
            else:
                points_slope = (next_point[1] - point[1]) / slope_dmtr

            if points_slope != slope:
                return False

        return True


def main():
    print(
        Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    )


if __name__ == "__main__":
    main()
