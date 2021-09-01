"""
URL of problem:
https://leetcode.com/problems/top-k-frequent-elements/
"""


from math import floor


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        # Build a min heap of size k. After heap
        # reaches size k, start popping off the
        # minimum after each addition. In the end,
        # only the least minimum values i.e.
        # the maximum values will be left.
        heap = []
        for idx, num in enumerate(counts):
            heap.append(num)
            if idx < k:
                self.buildMinHeap(heap, idx, counts)
            else:
                self.buildMinHeap(heap, k, counts)
                heap[0], heap[-1] = heap[-1], heap[0]
                heap.pop()
                self.minHeapify(heap, 0, counts, k)

        return heap


    def buildMinHeap(self, heap, idx, counts):
        parent_idx = int(floor((idx-1)/2))
        if parent_idx < 0:
            return

        if counts[heap[parent_idx]] > counts[heap[idx]]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            self.buildMinHeap(heap, parent_idx, counts)


    def minHeapify(self, heap, idx, counts, size):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        lowest_count_idx = idx

        if left_child_idx < size and counts[heap[idx]] > counts[heap[left_child_idx]]:
            lowest_count_idx = left_child_idx

        if right_child_idx < size and counts[heap[lowest_count_idx]] > counts[heap[right_child_idx]]:
            lowest_count_idx = right_child_idx

        if lowest_count_idx != idx:
            heap[idx], heap[lowest_count_idx] = heap[lowest_count_idx], heap[idx]
            self.minHeapify(heap, lowest_count_idx, counts, size)


def main():
    print(Solution().topKFrequent([3, 0, 1, 0], 1))


if __name__ == "__main__":
    main()
