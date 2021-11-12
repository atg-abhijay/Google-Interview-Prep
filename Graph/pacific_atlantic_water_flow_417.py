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


    def pacificAtlantic_2ndPass(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows, num_cols = len(heights), len(heights[0])
        if num_rows == 1 or num_cols == 1:
            return [[row_idx, col_idx] for row_idx, col_idx in product(range(num_rows), range(num_cols))]

        # [x, y, z] = [reach Pacific, reach Atlantic, visited]
        grid_flows = [[[0, 0, 0] for _ in range(num_cols)] for _ in range(num_rows)]
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            if grid_flows[row_idx][col_idx][:2] != [1, 1]:
                grid_flows[row_idx][col_idx][2] = 1
                self.runDFS((heights, grid_flows), (row_idx, col_idx), (num_rows, num_cols))
                # print()

        result = []
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            if grid_flows[row_idx][col_idx][:2] == [1, 1]:
                result.append([row_idx, col_idx])

        return result


    def runDFS(self, matrices, idxs, lengths):
        heights, grid_flows = matrices
        row_idx, col_idx = idxs
        num_rows, num_cols = lengths
        cell_info = grid_flows[row_idx][col_idx]
        # print(f"(Row, Column): ({row_idx}, {col_idx}), Height: {heights[row_idx][col_idx]}")
        if row_idx == 0 or col_idx == 0:
            cell_info[0] = 1

        if row_idx == num_rows - 1 or col_idx == num_cols - 1:
            cell_info[1] = 1

        if cell_info[:2] == [1, 1]:
            return

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        cell_height = heights[row_idx][col_idx]
        for row_diff, col_diff in directions:
            nbr_row, nbr_col = row_idx + row_diff, col_idx + col_diff
            within_bounds = 0 <= nbr_row < num_rows and 0 <= nbr_col < num_cols
            if within_bounds and heights[nbr_row][nbr_col] <= cell_height:
                if grid_flows[nbr_row][nbr_col][2] == 0:
                    grid_flows[nbr_row][nbr_col][2] = 1
                    self.runDFS(matrices, (nbr_row, nbr_col), lengths)
                    grid_flows[nbr_row][nbr_col][2] = 0

                nbr_info = grid_flows[nbr_row][nbr_col]
                cell_info[0] |= nbr_info[0]
                cell_info[1] |= nbr_info[1]

        return


def main():
    print(Solution().pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]))


if __name__ == "__main__":
    main()
