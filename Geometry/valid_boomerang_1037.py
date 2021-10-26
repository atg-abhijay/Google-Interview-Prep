"""
URL of problem:
https://leetcode.com/problems/valid-boomerang/
"""


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if any([points[0] == points[1], points[0] == points[2], points[1] == points[2]]):
            return False

        slope_1 = self.calculateSlope(points[0], points[1])
        slope_2 = self.calculateSlope(points[1], points[2])

        return slope_1 != slope_2


    def calculateSlope(self, point_a, point_b):
        slope_dmtr = point_b[0] - point_a[0]
        if slope_dmtr == 0:
            return float('inf')

        return (point_b[1] - point_a[1]) / slope_dmtr


def main():
    print(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]]))


if __name__ == "__main__":
    main()
