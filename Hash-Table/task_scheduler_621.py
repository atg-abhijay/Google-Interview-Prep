"""
URL of problem:
https://leetcode.com/problems/task-scheduler/
"""


import string
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cooldown_left = {letter: 0 for letter in string.ascii_uppercase}
        task_counts = {}
        for task in tasks:
            if task not in task_counts:
                task_counts[task] = 1
            else:
                task_counts[task] += 1

        heap = []
        for task, count in task_counts.items():
            heapq.heappush(heap, (-1 * count, task))

        total_time = 0
        while heap:
            count, top_task = heapq.heappop(heap)
            temp_storage = []
            is_idle = False
            while cooldown_left[top_task]:
                temp_storage.append((count, top_task))
                if heap:
                    count, top_task = heapq.heappop(heap)
                else:
                    is_idle = True
                    break

            total_time += 1
            for task, time_left in cooldown_left.items():
                cooldown_left[task] = max(0, time_left - 1)

            while temp_storage:
                heapq.heappush(heap, temp_storage.pop())

            if is_idle:
                continue

            count += 1
            if count != 0:
                heapq.heappush(heap, (count, top_task))
                cooldown_left[top_task] = n

        return total_time


def main():
    print(
        Solution().leastInterval(
            ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
        )
    )


if __name__ == "__main__":
    main()
