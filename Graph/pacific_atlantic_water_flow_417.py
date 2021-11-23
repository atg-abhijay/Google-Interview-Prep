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
        self.heights = None
        self.num_rows = 0
        self.num_cols = 0
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


    def pacificAtlantic_2ndPass(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.heights = heights
        self.num_rows, self.num_cols = len(heights), len(heights[0])
        grid_idxs = (range(self.num_rows), range(self.num_cols))
        if self.num_rows == 1 or self.num_cols == 1:
            return [[row_idx, col_idx] for row_idx, col_idx in product(*grid_idxs)]

        pacific_cells, atlantic_cells = set(), set()
        for row_idx in range(self.num_rows):
            self.runDFS((row_idx, 0), pacific_cells)
            self.runDFS((row_idx, self.num_cols - 1), atlantic_cells)

        for col_idx in range(self.num_cols):
            self.runDFS((0, col_idx), pacific_cells)
            self.runDFS((self.num_rows - 1, col_idx), atlantic_cells)

        return list(pacific_cells.intersection(atlantic_cells))


    def runDFS(self, cell_idxs, ocean_cells):
        if cell_idxs in ocean_cells:
            return

        ocean_cells.add(cell_idxs)
        row_idx, col_idx = cell_idxs
        cell_height = self.heights[row_idx][col_idx]
        for row_diff, col_diff in self.directions:
            nbr_row, nbr_col = row_idx + row_diff, col_idx + col_diff
            within_bounds = 0 <= nbr_row < self.num_rows and 0 <= nbr_col < self.num_cols
            if within_bounds and self.heights[nbr_row][nbr_col] >= cell_height:
                self.runDFS((nbr_row, nbr_col), ocean_cells)

        return


def main():
    print(
        Solution().pacificAtlantic_2ndPass(
            [[78, 65, 50, 95], [0, 64, 98, 94], [19, 27, 27, 49]]
        )
    )


if __name__ == "__main__":
    main()
