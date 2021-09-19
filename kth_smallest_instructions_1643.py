"""
URL of problem:
https://leetcode.com/problems/kth-smallest-instructions/
"""


import heapq
from collections import deque
from math import comb


class Solution(object):
    def kthSmallestPath2(self, destination, k):
        target_row, target_col = destination
        path_length = target_row + target_col
        count = 0
        for num in range(1 << target_row - 1, 1 << path_length):
            if self.checkNumOneBits(num, target_row):
                count += 1

            if count == k:
                break

        kth_path_bits = bin(num)[2:].zfill(path_length)
        return ''.join(["H" if bit == "0" else "V" for bit in kth_path_bits])


    def checkNumOneBits(self, num, target):
        num_one_bits = 0
        while num > 0:
            num &= num - 1
            num_one_bits += 1

        return num_one_bits == target


    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        target_row, target_col = destination
        num_combinations = comb(target_row + target_col, target_row)
        # When using the heap, use a weight of -1 to make larger
        # values smaller so that these larger values are popped
        # from the heap, thereby only leaving the smaller values
        weight = -1
        if k > int(num_combinations/2):
            k = num_combinations - k + 1
            weight = 1

        kth_path = self.determinePaths([target_row, target_col, k], weight)
        kth_path_bits = bin(kth_path)[2:].zfill(target_row+target_col)
        return ''.join(["H" if bit == "0" else "V" for bit in kth_path_bits])


    def determinePaths(self, constants, weight):
        target_row, target_col, k = constants
        backward_dirns = [(0, -1), (-1, 0)]
        grid_paths = [[[] for _ in range(target_col+1)] for _ in range(target_row+1)]
        enqueued = [[0 for _ in range(target_col+1)] for _ in range(target_row+1)]
        queue = deque([(target_row, target_col)])
        grid_paths[target_row][target_col] = [(0, 0)]
        while queue:
            row_idx, col_idx = queue.popleft()
            if [row_idx, col_idx] == [0, 0]:
                break

            for decr_x, decr_y in backward_dirns:
                nbr_row, nbr_col = row_idx + decr_x, col_idx + decr_y
                within_bounds = 0 <= nbr_row <= target_row and 0 <= nbr_col <= target_col
                if not within_bounds:
                    continue

                if not enqueued[nbr_row][nbr_col]:
                    queue.append((nbr_row, nbr_col))
                    enqueued[nbr_row][nbr_col] = 1

                dirn = "H" if decr_y == -1 else "V"
                heap = grid_paths[nbr_row][nbr_col]
                steps_away = target_row + target_col - nbr_row - nbr_col - 1
                for path in grid_paths[row_idx][col_idx]:
                    nbr_path = (1 << steps_away if dirn == "V" else 0) | path[1]
                    heapq.heappush(heap, (weight * nbr_path, nbr_path))
                    if len(heap) > k:
                        heapq.heappop(heap)

        return heapq.heappop(grid_paths[0][0])[1]


def main():
    print(Solution().kthSmallestPath2([10, 9], 60000))


if __name__ == "__main__":
    main()
