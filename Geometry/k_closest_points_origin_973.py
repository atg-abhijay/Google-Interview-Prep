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


    def kClosest_2ndPass(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        k_closest = []
        num_added = 0
        for x, y in points:
            heapq.heappush(k_closest, (-1 * (x ** 2 + y ** 2), [x, y]))
            num_added += 1
            if num_added > k:
                heapq.heappop(k_closest)

        return [point for _, point in k_closest]


def main():
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))


if __name__ == "__main__":
    main()
