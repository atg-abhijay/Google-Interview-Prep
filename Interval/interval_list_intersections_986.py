"""
URL of problem:
https://leetcode.com/problems/interval-list-intersections/
"""


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
        ans = []
        # for f_intvl in firstList:
        #     for idx, s_intvl in enumerate(secondList[s_idx:]):
        #         if self.is_overlap(f_intvl, s_intvl):
        #             ans.append(self.find_intxn(f_intvl, s_intvl))
        #         else:
        #             s_idx += idx - 1

        did_reset = False
        while f_idx < f_len and s_idx < s_len:
            f_intvl, s_intvl = firstList[f_idx], secondList[s_idx]
            if self.is_overlap(f_intvl, s_intvl):
                ans.append(self.find_intxn(f_intvl, s_intvl))
                s_idx += 1
                did_reset = False
            else:
                if not did_reset:
                    s_idx -= 1
                    f_idx += 1
                    did_reset = True
                else:
                    s_idx += 1

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
