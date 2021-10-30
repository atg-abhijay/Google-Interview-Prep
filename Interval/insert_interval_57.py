"""
URL of problem:
https://leetcode.com/problems/insert-interval/
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        did_overlap_occur = False
        overlap_start, overlap_end = -1, len(intervals) - 1
        for idx, intvl in enumerate(intervals):
            if self.is_overlap(intvl, newInterval):
                if overlap_start == -1:
                    overlap_start = idx

                newInterval = self.merge_intervals(intvl, newInterval)
                did_overlap_occur = True

            # Overlaps are finished
            elif did_overlap_occur:
                overlap_end = idx-1
                break

            # No overlaps encountered yet
            elif newInterval[0] < intvl[0]:
                intervals.insert(idx, newInterval)
                return intervals

        if did_overlap_occur:
            for idx in range(overlap_end, overlap_start, -1):
                intervals.pop(idx)

            intervals[overlap_start] = newInterval
            return intervals

        # Case where interval is at the end of the list
        intervals.append(newInterval)
        return intervals


    def is_overlap(self, intvl_a, intvl_b):
        return intvl_a[0] <= intvl_b[1] and intvl_b[0] <= intvl_a[1]


    def merge_intervals(self, intvl_a, intvl_b):
        return [min(intvl_a[0], intvl_b[0]), max(intvl_a[1], intvl_b[1])]


    def insert_2ndPass(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        # If the new interval comes before all the intervals
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        ans = []
        did_find_overlap, did_insert = False, False
        for idx, intvl in enumerate(intervals):
            if self.is_overlap_2ndPass(intvl, newInterval):
                newInterval = self.merge_intervals_2ndPass(intvl, newInterval)
                did_find_overlap = True
            else:
                # If the overlap is coming to an end or the
                # new interval sits before the current interval
                if did_find_overlap or newInterval[1] < intvl[0]:
                    ans.append(newInterval)
                    did_insert = True
                    ans.extend(intervals[idx:])
                    break

                ans.append(intvl)

        if not did_insert:
            ans.append(newInterval)

        return ans


    def is_overlap_2ndPass(self, intvl_a, intvl_b):
        return intvl_a[0] <= intvl_b[1] and intvl_b[0] <= intvl_a[1]


    def merge_intervals_2ndPass(self, intvl_a, intvl_b):
        return [min(intvl_a[0], intvl_b[0]), max(intvl_a[1], intvl_b[1])]


def main():
    print(Solution().insert([[1, 5]], [2, 3]))


if __name__ == "__main__":
    main()
