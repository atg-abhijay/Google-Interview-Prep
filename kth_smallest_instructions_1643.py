"""
URL of problem:
https://leetcode.com/problems/kth-smallest-instructions/
"""


import heapq


class StringWrapper:
    def __init__(self, value: str):
        self.val = value

    # Use a reverse comparison to make
    # larger values smaller so that these
    # larger values are popped from the heap,
    # thereby only leaving the smaller values
    def __lt__(self, other):
        return other.val < self.val

    def add_path(self, path):
        self.val += path.val


class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        heap = []
        target_row, target_col = destination
        directions = [(0, 1), (1, 0)]
        grid = [[-1 for _ in range(target_col+1)] for _ in range(target_row+1)]
        grid_paths = [[[] for _ in range(target_col+1)] for _ in range(target_row+1)]
        self.performDFS([0, 0], [heap, grid, grid_paths, directions], [target_row, target_col, k])
        return heapq.heappop(grid_paths[0][0]).val


    def performDFS(self, indices, arrays, constants):
        row_idx, col_idx = indices
        heap, grid, grid_paths, directions = arrays
        target_row, target_col, k = constants

        if row_idx == target_row and col_idx == target_col:
            grid_paths[row_idx][col_idx] = [StringWrapper("")]

        for incr_x, incr_y in directions:
            nbr_row, nbr_col = row_idx + incr_x, col_idx + incr_y
            if 0 <= nbr_row <= target_row and 0 <= nbr_col <= target_col:
                if not grid_paths[nbr_row][nbr_col]:
                    self.performDFS([nbr_row, nbr_col], arrays, constants)

                dirn = "H" if incr_y == 1 else "V"
                for path in grid_paths[nbr_row][nbr_col]:
                    self.addPathForPosition(*indices, grid_paths, dirn, path, k)


    def addPathForPosition(self, row_idx, col_idx, grid_paths, dirn, path, k):
        new_path = StringWrapper(dirn)
        new_path.add_path(path)
        heap = grid_paths[row_idx][col_idx]
        heapq.heappush(heap, new_path)
        if len(heap) > k:
            heapq.heappop(heap)


def main():
    print(Solution().kthSmallestPath([2, 3], 1))


if __name__ == "__main__":
    main()
