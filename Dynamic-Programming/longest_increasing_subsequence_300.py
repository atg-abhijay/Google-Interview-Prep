"""
URL of problem:
https://leetcode.com/problems/longest-increasing-subsequence/
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        num_elems = len(nums)
        for combn in range(2 ** num_elems, 2 ** (num_elems + 1)):
            bitmask = bin(combn)[3:]
            sequence = [num for switch, num in zip(bitmask, nums) if switch == '1']
            if all(map(lambda xy: xy[0] < xy[1], zip(sequence, sequence[1:]))):
                max_length = max(max_length, len(sequence))

        return max_length


def main():
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == "__main__":
    main()
