"""
URL of problem:
https://leetcode.com/problems/number-of-provinces/
"""


from collections import deque


class Solution:
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # Time: O(#cities + #connections) - BFS runtime
        # Space: O(#cities) - for unvisited_cities and queue
        # Tags: Graphs, BFS
        num_provinces = 0
        unvisited_cities = set(range(len(isConnected)))
        while unvisited_cities:
            queue = deque([unvisited_cities.pop()])
            num_provinces += 1
            while queue:
                city = queue.popleft()
                for idx, is_nbr in enumerate(isConnected[city]):
                    if idx in unvisited_cities and is_nbr:
                        unvisited_cities.remove(idx)
                        queue.append(idx)

        return num_provinces


    def findCircleNum_DFS(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # A DFS solution
        num_provinces = 0
        unvisited_cities = set(range(len(isConnected)))
        while unvisited_cities:
            stack = [unvisited_cities.pop()]
            num_provinces += 1
            while stack:
                city = stack.pop()
                for idx, is_nbr in enumerate(isConnected[city]):
                    if idx in unvisited_cities and is_nbr:
                        unvisited_cities.remove(idx)
                        stack.append(idx)

        return num_provinces


def main():
    print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))


if __name__ == "__main__":
    main()
