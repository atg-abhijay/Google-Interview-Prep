"""
URL of problem:
https://leetcode.com/problems/flower-planting-with-no-adjacent/
"""


from collections import deque


class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # If the gardens don't have paths between them,
        # any flower can be planted in each of them
        if not paths:
            return [1] * n

        graph = [[] for _ in range(n+1)]
        for garden_x, garden_y in paths:
            graph[garden_x].append(garden_y)
            graph[garden_y].append(garden_x)

        visited, all_gardens = set(), set(range(1, n+1))
        all_flowers, answer = {1, 2, 3, 4}, [-1] * (n+1)
        while all_gardens:
            queue = deque([all_gardens.pop()])
            visited.add(queue[0])
            while queue:
                garden = queue.popleft()
                all_gardens.discard(garden)
                nbr_flowers = {answer[nbr] for nbr in graph[garden]}
                answer[garden] = all_flowers.difference(nbr_flowers).pop()
                for nbr_garden in graph[garden]:
                    if nbr_garden not in visited:
                        visited.add(nbr_garden)
                        queue.append(nbr_garden)

        return answer[1:]


def main():
    print(Solution().gardenNoAdj(4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))


if __name__ == "__main__":
    main()
