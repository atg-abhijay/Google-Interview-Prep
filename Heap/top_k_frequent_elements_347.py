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

        # Build a max heap
        heap = []
        for idx, num in enumerate(counts):
            heap.append(num)
            self.buildMaxHeap(heap, idx, counts)

        # Repeatedly move most frequent elements
        # to end of array and restore heap property
        last_idx = len(heap) - 1
        for _ in range(k):
            heap[0], heap[last_idx] = heap[last_idx], heap[0]
            self.maxHeapify(heap, 0, counts, last_idx)
            last_idx -= 1

        return heap[-k:]

    def buildMaxHeap(self, heap, idx, counts):
        parent_idx = int(floor((idx-1)/2))
        if parent_idx < 0:
            return

        if counts[heap[parent_idx]] < counts[heap[idx]]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            self.buildMaxHeap(heap, parent_idx, counts)


    def maxHeapify(self, heap, idx, counts, size):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        highest_count_idx = idx

        if left_child_idx < size and counts[heap[idx]] < counts[heap[left_child_idx]]:
            highest_count_idx = left_child_idx

        if right_child_idx < size and counts[heap[highest_count_idx]] < counts[heap[right_child_idx]]:
            highest_count_idx = right_child_idx

        if highest_count_idx != idx:
            heap[idx], heap[highest_count_idx] = heap[highest_count_idx], heap[idx]
            self.maxHeapify(heap, highest_count_idx, counts, size)


def main():
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))


if __name__ == "__main__":
    main()
