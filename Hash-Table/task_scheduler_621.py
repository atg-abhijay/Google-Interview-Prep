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
        task_details = {}
        for task in tasks:
            if task not in task_details:
                # [count, cooldown time left, is in heap]
                task_details[task] = [-1, 0, False]
            else:
                task_details[task][0] -= 1

        heap, total_time = [], 0
        while task_details:
            # Add all tasks that have zero cooldown time
            # left and are not in the heap, to the heap
            for task, values in task_details.items():
                count, cooldown_left, is_in_heap = values
                if cooldown_left == 0 and not is_in_heap:
                    heapq.heappush(heap, (count, task))
                    values[2] = True

            total_time += 1
            # Decrement the cooldown times
            for task, values in task_details.items():
                values[1] = max(0, values[1] - 1)

            # Idle
            if not heap:
                continue

            # Complete the task and update it's count.
            # Delete the task if the count reaches zero
            count, top_task = heapq.heappop(heap)
            count += 1
            if count == 0:
                del task_details[top_task]
            else:
                task_details[top_task] = [count, n, False]

        return total_time


def main():
    print(
        Solution().leastInterval(
            ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
        )
    )


if __name__ == "__main__":
    main()
