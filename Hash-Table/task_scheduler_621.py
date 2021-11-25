"""
URL of problem:
https://leetcode.com/problems/task-scheduler/
"""


from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)

        tasks_counts = Counter(tasks)
        top_task, max_count = tasks_counts.most_common(1)[0]
        cpu_heap, tasks_heap = [(0, -1 * max_count, top_task)], []
        del tasks_counts[top_task]
        for task, count in tasks_counts.items():
            # Use a negative count to emulate a max heap
            # Tuple: (permitted time, negative count, task)
            heapq.heappush(tasks_heap, (0, -1 * count, task))

        global_time = 0
        while cpu_heap:
            allowed_time, _, _ = cpu_heap[0]
            if global_time < allowed_time:
                if tasks_heap:
                    _, neg_count, top_task = heapq.heappop(tasks_heap)
                else:
                    global_time += 1
                    # print("idle -> ", end=" ")
                    continue
            else:
                _, neg_count, top_task = heapq.heappop(cpu_heap)

            # print(f"{top_task} -> ", end=" ")
            updated_count = neg_count + 1
            if updated_count != 0:
                heapq.heappush(cpu_heap, (global_time + n + 1, updated_count, top_task))

            global_time += 1

        # print()
        return global_time

        task_details = {}
        for task in tasks:
            # Use a negative count to emulate a max heap
            if task not in task_details:
                task_details[task] = -1
            else:
                task_details[task] -= 1

        # Push (remaining cooldown time, count, task)
        # The cooldown time will be the first
        # priority and then the count for the task
        cpu_heap, current_time = [], 0
        for task, count in task_details.items():
            heapq.heappush(cpu_heap, (0, count, task))

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

        while cpu_heap:
            # If the top priority task doesn't have a remaining
            # cooldown time of 0, then the CPU has to be idle
            if cpu_heap[0][0] == 0:
                _, count, top_task = heapq.heappop(cpu_heap)
                print(f"{top_task} -> ", end=" ")
                if count + 1 != 0:
                    heapq.heappush(cpu_heap, (n + 1, count + 1, top_task))
            else:
                print("idle -> ", end=" ")

            # Decrement the cooldown times and heapify the heap
            are_cooldowns_updated = False
            for idx, (cooldown_left, count, task) in enumerate(cpu_heap):
                if cooldown_left != 0:
                    cpu_heap[idx] = (max(0, cooldown_left - 1), count, task)
                    are_cooldowns_updated = True

            if are_cooldowns_updated:
                heapq.heapify(cpu_heap)

            current_time += 1

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
