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
        while cpu_heap or tasks_heap:
            if cpu_heap and global_time >= cpu_heap[0][0]:
                _, neg_count, top_task = heapq.heappop(cpu_heap)
            elif tasks_heap:
                _, neg_count, top_task = heapq.heappop(tasks_heap)
            else:
                global_time += 1
                # print("idle -> ", end=" ")
                continue

            # print(f"{top_task} -> ", end=" ")
            updated_count = neg_count + 1
            if updated_count != 0:
                heapq.heappush(cpu_heap, (global_time + n + 1, updated_count, top_task))

            global_time += 1

        # print()
        return global_time


def main():
    print(
        Solution().leastInterval(
            ["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], n = 7
        )
    )


if __name__ == "__main__":
    main()
