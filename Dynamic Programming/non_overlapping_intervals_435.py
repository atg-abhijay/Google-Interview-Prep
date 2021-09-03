"""
URL of problem:
https://leetcode.com/problems/non-overlapping-intervals/
"""


from bisect import bisect_right


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        num_intervals = len(intervals)
        # Sort the intervals by their finish times
        intervals.sort(key=lambda x: x[1])
        finish_times = [intvl[1] for intvl in intervals]
        # Determine most recent non-overlapping predecessors
        # Add a dummy predecessor at the beginning
        predecs = [0] * (num_intervals + 1)
        for i, interval in enumerate(intervals):
            predecs[i + 1] = bisect_right(finish_times, interval[0], hi=i)

        max_overlap = [0] * (num_intervals + 1)
        for idx in range(1, num_intervals + 1):
            max_overlap[idx] = max(1 + max_overlap[predecs[idx]], max_overlap[idx - 1])

        return num_intervals - max_overlap[-1]


def main():
    print(Solution().eraseOverlapIntervals([[1, 3], [4, 5], [2, 7], [3, 9], [8, 10]]))


if __name__ == "__main__":
    main()
