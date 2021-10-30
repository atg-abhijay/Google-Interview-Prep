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
        return [[]]


def main():
    print(Solution().merge([[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]))


if __name__ == "__main__":
    main()
