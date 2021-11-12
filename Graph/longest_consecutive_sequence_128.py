"""
URL of problem:
https://leetcode.com/problems/longest-consecutive-sequence/
"""


from collections import defaultdict


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        min_val, max_val = min(nums), max(nums)
        num_elems = len(nums)
        sequences = defaultdict(lambda: [0] * num_elems)
        for num in nums:
            quotient, remainder = num // num_elems, num % num_elems
            sequences[quotient][remainder] = 1

        longest_seq_len = 0
        min_quotient, max_quotient = min_val // num_elems, max_val // num_elems
        for quotient in range(min_quotient, max_quotient+1):
            if quotient not in sequences:
                continue

            longest_seq_len = max(longest_seq_len, self.get_cnsctv_ones(sequences[quotient]))
            if quotient + 1 in sequences:
                longest_seq_len = max(longest_seq_len, self.get_cnsctv_ones(sequences[quotient] + sequences[quotient + 1]))

        return longest_seq_len


    def get_cnsctv_ones(self, sequence):
        num_consecutive = max_consecutive = 0
        for num in sequence:
            if num == 1:
                num_consecutive += 1
            else:
                max_consecutive = max(max_consecutive, num_consecutive)
                num_consecutive = 0

        return max(max_consecutive, num_consecutive)


def main():
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


if __name__ == "__main__":
    main()
