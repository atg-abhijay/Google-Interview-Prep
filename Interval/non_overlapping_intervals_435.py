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
            predecs[i + 1] = self.findPredecessor(finish_times, interval[0], i)

        opt_intvls = [0] * (num_intervals + 1)
        for idx in range(1, num_intervals + 1):
            opt_intvls[idx] = max(1 + opt_intvls[predecs[idx]], opt_intvls[idx - 1])

        return num_intervals - opt_intvls[-1]


    def findPredecessor(self, finish_times, start_time, intvl_idx):
        pred_idx = bisect_right(finish_times, x=start_time, hi=intvl_idx)
        if pred_idx == 0 and finish_times[0] == start_time:
            return 1

        return pred_idx


def main():
    print(Solution().eraseOverlapIntervals([[1, 3], [4, 5], [2, 7], [3, 9], [8, 10]]))


if __name__ == "__main__":
    main()
