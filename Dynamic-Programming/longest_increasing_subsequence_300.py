"""
URL of problem:
https://leetcode.com/problems/longest-increasing-subsequence/
"""


import heapq


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2), Space: O(n)
        # Tags: Dynamic Programming

        # sequence_lengths[i] will store the sequence
        # length that can be achieved by -
        # 1. considering the numbers upto index i,
        # 2. _selecting_ the number at index i
        #
        # When we select the number at index i, we then must
        # search for the rightmost smaller number which has
        # the greatest sequence length associated with it.
        #
        # We keep track of the maximum length separately
        # since sequence_lengths is storing the best
        # lengths that can be obtained when we fix a
        # choice of picking the number at index i. Due to
        # that, the lengths in the list aren't in
        # consistently increasing order.
        max_length, sequence_lengths = 1, [1] * len(nums)
        for idx, num in enumerate(nums):
            rightmost_smaller_idx, greatest_ln = -1, 0
            for j, prev in enumerate(nums[:idx]):
                if prev < num and sequence_lengths[j] > greatest_ln:
                    rightmost_smaller_idx = j
                    greatest_ln = sequence_lengths[j]

            if rightmost_smaller_idx != -1:
                sequence_lengths[idx] = 1 + greatest_ln

            max_length = max(max_length, sequence_lengths[idx])

        return max_length


    def lengthOfLIS_alternate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Attempt an alternate solution to try to achieve
        # O(nlogn) time complexity. Unfortunately, this doesn't
        # achieve it. Running time is quite bad - ~9800 ms, 5%
        max_length, sequence_lengths = 1, [1] * len(nums)
        heap = []
        for idx, num in enumerate(nums):
            temp_storage = []
            while heap:
                seq_length, _, rightmost_idx = heap[0]
                if nums[rightmost_idx] < num:
                    sequence_lengths[idx] = 1 + (-1 * seq_length)
                    break

                temp_storage.append(rightmost_idx)
                heapq.heappop(heap)

            while temp_storage:
                p_idx = temp_storage.pop()
                heapq.heappush(heap, (-1 * sequence_lengths[p_idx], -1 * p_idx, p_idx))

            heapq.heappush(heap, (-1 * sequence_lengths[idx], -1 * idx, idx))
            max_length = max(max_length, sequence_lengths[idx])

        return max_length


def main():
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == "__main__":
    main()
