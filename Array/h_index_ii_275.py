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
        start, stop = 0, num_citns - 1
        max_h_val = -1
        while start < stop - 1:
            middle_idx = (start + stop) // 2
            middle_citn = citations[middle_idx]
            if num_citns - middle_idx >= middle_citn:
                max_h_val = max(max_h_val, middle_citn)
                start = middle_idx
            else:
                stop = middle_idx

        return max_h_val


def main():
    print(Solution().hIndex([0, 1, 3, 5, 6]))


if __name__ == "__main__":
    main()
