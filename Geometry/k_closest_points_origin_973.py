"""
URL of problem:
https://leetcode.com/problems/k-closest-points-to-origin/
"""


import heapq


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for idx, point in enumerate(points):
            heapq.heappush(heap, (-1 * (point[0] ** 2 + point[1] ** 2), point))
            if idx >= k:
                heapq.heappop(heap)

        return [elem[1] for elem in heap]


def main():
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))


if __name__ == "__main__":
    main()
