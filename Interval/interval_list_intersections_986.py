"""
URL of problem:
https://leetcode.com/problems/interval-list-intersections/
"""


from bisect import bisect_left


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        # Let length of the lists be m, n.
        # Time:
        # - m instances of binary search: O(mlogn)
        # - m instances of iterating on a subarray: O(n) I think
        # - Therefore: O(mlogn) + O(n)
        # Space: O(n)
        # Tags: Intervals, Binary Search, Sorting
        ans, second_list_starts = [], [intvl[0] for intvl in secondList]
        prev_search_idx = 0
        for f_intvl in firstList:
            search_idx = bisect_left(second_list_starts, f_intvl[1] + 1)
            for s_intvl in secondList[prev_search_idx:search_idx]:
                if self.is_overlap(f_intvl, s_intvl):
                    ans.append(self.find_intxn(f_intvl, s_intvl))

            prev_search_idx = max(0, search_idx - 1)

        return ans


    def is_overlap(self, intvl_a, intvl_b):
        return intvl_a[0] <= intvl_b[1] and intvl_b[0] <= intvl_a[1]


    def find_intxn(self, intvl_a, intvl_b):
        return [max(intvl_a[0], intvl_b[0]), min(intvl_a[1], intvl_b[1])]


def main():
    print(
        Solution().intervalIntersection(
            [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
        )
    )


if __name__ == "__main__":
    main()
