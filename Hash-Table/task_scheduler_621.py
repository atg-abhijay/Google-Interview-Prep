"""
URL of problem:
https://leetcode.com/problems/task-scheduler/
"""


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
            # Use a negative count to emulate a max heap
            if task not in task_details:
                task_details[task] = -1
            else:
                task_details[task] -= 1

        heap, current_time = [], 0
        for task, count in task_details.items():
            # Push (remaining cooldown time, count, task)
            # The cooldown time will be the first priority
            # and then the count for the task
            heapq.heappush(heap, (0, count, task))

        # Alternate approach:
        # Here, the cooldown time is not decremented.
        # Rather, the current time is incremented and
        # that is used as a basis for selecting the
        # next task. Still giving problems though.
        # while heap:
        #     if heap[0][0] > current_time:
        #         print("idle -> ", end=" ")
        #     else:
        #         _, count, top_task = heapq.heappop(heap)
        #         print(f"{top_task} -> ", end=" ")
        #         if count + 1 != 0:
        #             heapq.heappush(heap, (n + current_time + 1, count + 1, top_task))

        #     current_time += 1

        # return current_time

        while heap:
            current_time += 1
            # If the top priority task doesn't have a remaining
            # cooldown time of 0, then the CPU has to be idle
            is_idle = False
            if heap[0][0] != 0:
                print("idle -> ", end=" ")
                is_idle = True

            # Decrement the cooldown times
            for idx, (cooldown_left, count, task) in enumerate(heap):
                heap[idx] = (max(0, cooldown_left - 1), count, task)

            if is_idle:
                continue

            _, count, top_task = heapq.heappop(heap)
            print(f"{top_task} -> ", end=" ")
            if count + 1 != 0:
                heapq.heappush(heap, (n, count + 1, top_task))

        print()
        return current_time


def main():
    print(
        Solution().leastInterval(
            ["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], n = 7
        )
    )


if __name__ == "__main__":
    main()
