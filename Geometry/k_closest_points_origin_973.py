"""
URL of problem:
https://leetcode.com/problems/k-closest-points-to-origin/
"""


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        """
        This question can be re-examined
        once I look into Heaps.
        """
        points.sort(key=lambda coords: coords[0] ** 2 + coords[1] ** 2)
        return points[:k]


def main():
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))


if __name__ == "__main__":
    main()
