"""
URL of problem:
https://leetcode.com/problems/top-k-frequent-elements/
"""


from collections import Counter, deque
import heapq
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


    def topKFrequent_2ndPass(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        heap, size = [], 0
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            size += 1
            if size > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]


    def topKFrequent_alternative_2ndPass(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        heap, size = deque(), 0
        for num, count in counts.items():
            heap.append((num, count))
            size += 1
            self.bubbleUp(heap, size - 1)
            if size > k:
                heap.popleft()
                heap.appendleft(heap.pop())
                self.bubbleDown(heap, 0, k)
                size = k

        return [item[0] for item in heap]


    def bubbleUp(self, heap, idx):
        if idx == 0:
            return

        parent_idx = floor((idx - 1)/2)
        if heap[idx][1] < heap[parent_idx][1]:
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
            self.bubbleUp(heap, parent_idx)

        return


    def bubbleDown(self, heap, idx, size_limit):
        if idx >= size_limit:
            return

        left_idx, right_idx = 2 * idx + 1, 2 * idx + 2
        left_count = heap[left_idx][1] if left_idx < size_limit else float('inf')
        right_count = heap[right_idx][1] if right_idx < size_limit else float('inf')

        if left_idx >= size_limit and right_idx >= size_limit:
            return

        min_idx = left_idx if left_count < right_count else right_idx

        if heap[idx][1] > heap[min_idx][1]:
            heap[idx], heap[min_idx] = heap[min_idx], heap[idx]
            self.bubbleDown(heap, min_idx, size_limit)

        return


def main():
    print(Solution().topKFrequent([3, 0, 1, 0], 1))


if __name__ == "__main__":
    main()
