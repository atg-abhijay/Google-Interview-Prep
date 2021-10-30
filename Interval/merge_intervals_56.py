"""
URL of problem:
https://leetcode.com/problems/merge-intervals/
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        prev_interval = [-1, -1]
        for intvl in intervals:
            if self.is_overlap(intvl, prev_interval):
                merged_intervals[-1] = [min(intvl[0], prev_interval[0]), max(intvl[1], prev_interval[1])]
            else:
                merged_intervals.append(intvl)

            prev_interval = merged_intervals[-1]

        return merged_intervals


    def is_overlap(self, intvl_a, intvl_b):
        return intvl_a[0] <= intvl_b[1] and intvl_b[0] <= intvl_a[1]


    def merge_2ndPass(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Half-working solution
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 1:
            return intervals

        ans, overlapping_intvl = [], intervals[0]
        did_overlap_occur = False
        for idx, intvl in enumerate(intervals):
            if self.is_overlap_2ndPass(intvl, overlapping_intvl):
                overlapping_intvl = self.merge_two_intvls_2ndPass(intvl, overlapping_intvl)
                did_overlap_occur = True
            else:
                if did_overlap_occur:
                    ans.append(overlapping_intvl)
                    did_overlap_occur = False
                    overlapping_intvl = intvl

                else:
                    ans.append(intvl)

        if did_overlap_occur:
            ans.append(overlapping_intvl)

        return ans


        while 1:
            ans, overlapping_intvl = [], intervals[0]
            did_overlap_occur, did_update = False, False
            for idx, intvl in enumerate(intervals[1:]):
                if self.is_overlap_2ndPass(intvl, overlapping_intvl):
                    overlapping_intvl = self.merge_two_intvls_2ndPass(intvl, overlapping_intvl)
                    did_overlap_occur = True
                else:
                    if did_overlap_occur:
                        ans.append(overlapping_intvl)
                        ans.extend(intervals[idx+1:])
                        did_update = True
                        break

                    ans.append(intvl)
                    overlapping_intvl = intvl

            if not did_overlap_occur:
                return intervals

            if not did_update:
                ans.append(overlapping_intvl)

            intervals = ans


    def is_overlap_2ndPass(self, intvl_a, intvl_b):
        return intvl_a[0] <= intvl_b[1] and intvl_b[0] <= intvl_a[1]


    def merge_two_intvls_2ndPass(self, intvl_a, intvl_b):
        return [min(intvl_a[0], intvl_b[0]), max(intvl_a[1], intvl_b[1])]


def main():
    print(Solution().merge_2ndPass([[1,3],[2,6],[8,10],[15,18]]))


if __name__ == "__main__":
    main()
