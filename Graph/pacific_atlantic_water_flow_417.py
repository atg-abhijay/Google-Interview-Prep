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
        reachable_oceans = [[[0, 0] for _ in range(num_cols)] for _ in range(num_rows)]
        lambda_nbr = lambda args: self.checkNeighbor(reachable_oceans, heights, *args)

        in_order_ranges = (range(num_rows), range(num_cols))
        reverse_ranges = (range(num_rows - 1, -1, -1), range(num_cols - 1, -1, -1))
        eval_nbr = {
            'n': lambda r, c, ocean: lambda_nbr([r-1 >= 0, [r, c], [r-1, c], ocean]),
            'w': lambda r, c, ocean: lambda_nbr([c-1 >= 0, [r, c], [r, c-1], ocean]),
            'e': lambda r, c, ocean: lambda_nbr([c+1 < num_cols, [r, c], [r, c+1], ocean]),
            's': lambda r, c, ocean: lambda_nbr([r+1 < num_rows, [r, c], [r+1, c], ocean])
        }

        ## Initial pass
        # Check reachability to Pacific Ocean
        for row_idx, col_idx in product(*in_order_ranges):
            # Check West and North neighbors
            args = [row_idx, col_idx, 0]
            eval_nbr['w'](*args)
            eval_nbr['n'](*args)

        # Check reachability to Atlantic Ocean
        for row_idx, col_idx in product(*reverse_ranges):
            # Check East and South neighbors
            args = [row_idx, col_idx, 1]
            eval_nbr['e'](*args)
            eval_nbr['s'](*args)

        # for row_idx, col_idx in product(*in_order_ranges):

        for idx_ranges in [in_order_ranges, reverse_ranges]:
            for ocean in [0, 1]:
                for row_idx, col_idx in product(*idx_ranges):
                    args = [row_idx, col_idx, ocean]
                    for dirn in ['w', 'n', 'e', 's']:
                        eval_nbr[dirn](*args)

        # ## Final pass
        # # Check reachability to Pacific Ocean
        # for row_idx, col_idx in product(*reverse_ranges):
        #     # Check East and South neighbors
        #     args = [row_idx, col_idx, 0]
        #     eval_nbr['e'](*args)
        #     eval_nbr['s'](*args)

        # # Check reachability to Atlantic Ocean
        # for row_idx, col_idx in product(*in_order_ranges):
        #     # Check West and North neighbors
        #     args = [row_idx, col_idx, 1]
        #     eval_nbr['w'](*args)
        #     eval_nbr['n'](*args)

        # Determine reachability to both oceans
        result = []
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            bool_oceans = reachable_oceans[row_idx][col_idx]
            if [row_idx, col_idx] == [11, 3]:
                print([row_idx, col_idx], ":", bool_oceans)
            if bool_oceans[0] and bool_oceans[1]:
                print([row_idx, col_idx], ":", bool_oceans)
                result.append([row_idx, col_idx])

        return result


    def checkNeighbor(self, reachable_oceans, heights, within_bounds, location, nbr, ocean):
        current_height = heights[location[0]][location[1]]
        oceans_for_loc = reachable_oceans[location[0]][location[1]]

        if within_bounds:
            if current_height >= heights[nbr[0]][nbr[1]]:
                nbr_tile = reachable_oceans[nbr[0]][nbr[1]]
                oceans_for_loc[ocean] |= nbr_tile[ocean]
        elif nbr < location:
            oceans_for_loc[0] = 1
        elif nbr > location:
            oceans_for_loc[1] = 1


def main():
    grid = [[8,13,11,18,14,16,16,4,4,8,10,11,1,19,7],[2,9,15,16,14,5,8,15,9,5,14,6,10,15,5],[15,16,17,10,3,6,3,4,2,17,0,12,4,1,3],[13,6,13,15,15,16,4,10,7,4,19,19,4,9,13],[7,1,9,14,9,11,5,4,15,19,6,0,0,13,5],[9,9,15,12,15,5,1,1,18,1,2,16,15,18,9],[13,0,4,18,12,0,11,0,1,15,1,15,4,2,0],[11,13,12,16,9,18,6,8,18,1,5,12,17,13,5],[7,17,2,5,0,17,9,18,4,13,6,13,7,2,1],[2,3,9,0,19,6,6,15,14,4,8,1,19,5,9],[3,10,5,11,7,14,1,5,3,19,12,5,2,13,16],[0,8,10,18,17,5,5,8,2,11,5,16,4,9,14],[15,9,16,18,9,5,2,5,13,3,10,19,9,14,3],[12,11,16,1,10,12,6,18,6,6,18,10,9,5,2],[17,9,6,6,14,9,2,2,13,13,15,17,15,3,14],[18,14,12,6,18,16,4,10,19,5,6,8,9,1,6]]
    # for row in grid:
    #     for elem in row:
    #         print(f'{elem:02}', end='\t')
    #     print()
    print(Solution().pacificAtlantic(grid))
    # print(
    #     Solution().pacificAtlantic([
    #         [1, 2, 3],
    #         [8, 9, 4],
    #         [7, 6, 5]
    #     ])
    # )


if __name__ == "__main__":
    main()
