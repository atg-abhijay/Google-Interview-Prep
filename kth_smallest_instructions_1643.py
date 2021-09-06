"""
URL of problem:
https://leetcode.com/problems/kth-smallest-instructions/
"""


import heapq
from collections import deque
from math import comb


class StringWrapper:
    def __init__(self, value: str):
        self.val = [value]

    def add_path(self, path):
        self.val.extend(path.val)


class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        target_row, target_col = destination
        num_combinations = comb(target_row + target_col, target_row)
        if k > int(num_combinations/2):
            k = num_combinations - k + 1
            StringWrapper.__lt__ = lambda self, other: self.val < other.val
        else:
            # Use a reverse comparison to make
            # larger values smaller so that these
            # larger values are popped from the heap,
            # thereby only leaving the smaller values
            StringWrapper.__lt__ = lambda self, other: other.val < self.val

        grid_paths = [[[] for _ in range(target_col+1)] for _ in range(target_row+1)]
        self.determinePaths(grid_paths, [target_row, target_col, k])
        return ''.join(heapq.heappop(grid_paths[0][0]).val)


    def determinePaths(self, grid_paths, constants):
        target_row, target_col, k = constants
        backward_dirns = [(0, -1), (-1, 0)]
        enqueued = [[0 for _ in range(target_col+1)] for _ in range(target_row+1)]
        dq = deque([(target_row, target_col)])
        grid_paths[target_row][target_col] = [StringWrapper("")]
        while dq:
            row_idx, col_idx = dq.popleft()
            if [row_idx, col_idx] == [0, 0]:
                break
            for decr_x, decr_y in backward_dirns:
                nbr_row, nbr_col = row_idx + decr_x, col_idx + decr_y
                within_bounds = 0 <= nbr_row <= target_row and 0 <= nbr_col <= target_col
                if within_bounds:
                    if not enqueued[nbr_row][nbr_col]:
                        dq.append((nbr_row, nbr_col))
                        enqueued[nbr_row][nbr_col] = 1

                    dirn = "H" if decr_y == -1 else "V"
                    for path in grid_paths[row_idx][col_idx]:
                        self.addPathForPosition(nbr_row, nbr_col, grid_paths, dirn, path, k)

            # Clear out the paths since they
            # have been added to the neighbors now
            grid_paths[row_idx][col_idx] = []


    def addPathForPosition(self, row_idx, col_idx, grid_paths, dirn, path, k):
        new_path = StringWrapper(dirn)
        new_path.add_path(path)
        heap = grid_paths[row_idx][col_idx]
        heapq.heappush(heap, new_path)
        if len(heap) > k:
            heapq.heappop(heap)


def main():
    print(Solution().kthSmallestPath([2, 3], 2))


if __name__ == "__main__":
    main()
