"""
URL of problem:
https://leetcode.com/problems/interval-list-intersections/
"""


from itertools import product


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if bool(firstList) ^ bool(secondList):
            return []

        f_idx, s_idx = 0, 0
        f_len, s_len = len(firstList), len(secondList)
        if s_len > f_len:
            firstList, secondList = secondList, firstList
            f_len, s_len = s_len, f_len

        ans = []
        for f_intvl, s_intvl in product(firstList, secondList):
            if self.is_overlap(f_intvl, s_intvl):
                ans.append(self.find_intxn(f_intvl, s_intvl))

        return ans

        # did_reset, ans = False, []
        # while f_idx < f_len:
        #     f_intvl, s_intvl = firstList[f_idx], secondList[s_idx]
        #     if self.is_overlap(f_intvl, s_intvl):
        #         ans.append(self.find_intxn(f_intvl, s_intvl))
        #         s_idx = min(s_len - 1, s_idx + 1)
        #         did_reset = False
        #     else:
        #         if not did_reset:
        #             s_idx = max(0, s_idx - 1)
        #             f_idx += 1
        #             did_reset = True
        #         else:
        #             s_idx += 1
        # return ans


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
