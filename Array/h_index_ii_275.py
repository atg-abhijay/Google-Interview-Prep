"""
URL of problem:
https://leetcode.com/problems/h-index-ii/
"""


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        num_citns = len(citations)
        if num_citns <= citations[0]:
            return num_citns

        start, stop, max_h_index = 0, num_citns, 0
        while start < stop:
            middle_idx = (start + stop) // 2
            middle_citn = citations[middle_idx]
            num_papers = num_citns - middle_idx
            if num_papers <= middle_citn:
                max_h_index = max(max_h_index, num_papers)
                stop = middle_idx
            else:
                start = middle_idx + 1

        return max_h_index


def main():
    print(Solution().hIndex([0, 1, 3, 5, 6]))


if __name__ == "__main__":
    main()
