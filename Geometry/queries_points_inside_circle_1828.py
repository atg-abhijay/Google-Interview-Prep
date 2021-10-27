"""
URL of problem:
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""


class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
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
        return []


def main():
    print(
        Solution().countPoints(
            [[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        )
    )


if __name__ == "__main__":
    main()
