"""
URL of problem:
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""


from itertools import product


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows, num_cols = len(heights), len(heights[0])
        range_rows, range_cols = range(num_rows), range(num_cols)
        visited = [[0 for _ in range_cols] for _ in range_rows]
        oceans = [[[0, 0] for _ in range_cols] for _ in range_rows]

        for row_idx, col_idx in product(range_rows, range_cols):
            self.performDFS([visited, oceans, heights], row_idx, col_idx, [num_rows, num_cols])

        for row_idx, col_idx in product(range_rows, range_cols):
            nbr_data = self.getNeighborData(row_idx, col_idx, num_rows, num_cols)
            for within_bounds, nbr_row, nbr_col, _ in nbr_data.values():
                if within_bounds and heights[row_idx][col_idx] >= heights[nbr_row][nbr_col]:
                    for ocean in [0, 1]:
                        oceans[row_idx][col_idx][ocean] |= oceans[nbr_row][nbr_col][ocean]

        result = []
        for row_idx, col_idx in product(range_rows, range_cols):
            if oceans[row_idx][col_idx] == [1, 1]:
                result.append([row_idx, col_idx])

        return result


    def performDFS(self, arrays, row_idx, col_idx, sizes):
        visited, oceans, heights = arrays
        num_rows, num_cols = sizes

        cell_height = heights[row_idx][col_idx]
        visited[row_idx][col_idx] = 1
        nbr_data = self.getNeighborData(row_idx, col_idx, num_rows, num_cols)
        for within_bounds, nbr_row, nbr_col, ocean in nbr_data.values():
            if within_bounds:
                if cell_height >= heights[nbr_row][nbr_col]:
                    if not visited[nbr_row][nbr_col]:
                        self.performDFS(arrays, nbr_row, nbr_col, sizes)

                    for ocn in [0, 1]:
                        oceans[row_idx][col_idx][ocn] |= oceans[nbr_row][nbr_col][ocn]

            else:
                oceans[row_idx][col_idx][ocean] = 1


    def getNeighborData(self, row_idx, col_idx, num_rows, num_cols):
        return {
            'n': [row_idx - 1 >= 0, row_idx-1, col_idx, 0],
            'e': [col_idx + 1 < num_cols, row_idx, col_idx+1, 1],
            'w': [col_idx - 1 >= 0, row_idx, col_idx-1, 0],
            's': [row_idx + 1 < num_rows, row_idx+1, col_idx, 1]
        }


    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.visited = set()
        self.atlantic_cells = set()
        self.pacific_cells = set()
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


    def pacificAtlantic_2ndPass(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.num_rows, self.num_cols = len(heights), len(heights[0])
        grid_idxs = (range(self.num_rows), range(self.num_cols))
        if self.num_rows == 1 or self.num_cols == 1:
            return [[row_idx, col_idx] for row_idx, col_idx in product(*grid_idxs)]

        for row_idx, col_idx in product(*grid_idxs):
            cell_idxs = (row_idx, col_idx)
            if cell_idxs not in self.pacific_cells or cell_idxs not in self.atlantic_cells:
                self.runDFS(heights, cell_idxs)

        return list(self.pacific_cells.intersection(self.atlantic_cells))


    def runDFS(self, heights, cell_idxs):
        row_idx, col_idx = cell_idxs
        if row_idx == 0 or col_idx == 0:
            self.pacific_cells.add(cell_idxs)

        if row_idx == self.num_rows - 1 or col_idx == self.num_cols - 1:
            self.atlantic_cells.add(cell_idxs)

        if cell_idxs in self.pacific_cells and cell_idxs in self.atlantic_cells:
            return

        cell_height = heights[row_idx][col_idx]
        for row_diff, col_diff in self.directions:
            nbr_row, nbr_col = row_idx + row_diff, col_idx + col_diff
            within_bounds = 0 <= nbr_row < self.num_rows and 0 <= nbr_col < self.num_cols
            if within_bounds and heights[nbr_row][nbr_col] <= cell_height:
                nbr_idxs = (nbr_row, nbr_col)
                if nbr_idxs not in self.visited:
                    self.visited.add(nbr_idxs)
                    self.runDFS(heights, nbr_idxs)

                if nbr_idxs in self.pacific_cells:
                    self.pacific_cells.add(cell_idxs)

                if nbr_idxs in self.atlantic_cells:
                    self.atlantic_cells.add(cell_idxs)

        # self.visited.remove(cell_idxs)
        return


def main():
    print(
        Solution().pacificAtlantic_2ndPass(
            [[78, 65, 50, 95], [0, 64, 98, 94], [19, 27, 27, 49]]
        )
    )


if __name__ == "__main__":
    main()
