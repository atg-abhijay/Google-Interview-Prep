"""
URL of problem:
https://leetcode.com/problems/keys-and-rooms/
"""


from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # Time: O(#rooms + #keys), Space: O(#rooms)
        # Tags: Graphs, DFS
        unvisited_rooms = set(range(len(rooms)))
        queue = deque([0])
        unvisited_rooms.discard(0)
        while queue:
            room = queue.popleft()
            for nbr in rooms[room]:
                if nbr in unvisited_rooms:
                    unvisited_rooms.discard(nbr)
                    queue.append(nbr)

        if unvisited_rooms:
            return False

        return True


def main():
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))


if __name__ == "__main__":
    main()
