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
        num_rows = len(heights)
        num_cols = len(heights[0])
        reachable_oceans = [[[0, 0] for _ in range(num_cols)] for _ in range(num_rows)]

        # Check reachability to Pacific Ocean
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            current_height = heights[row_idx][col_idx]
            # Check West neighbor
            if col_idx - 1 >= 0:
                if current_height >= heights[row_idx][col_idx-1]:
                    reachable_oceans[row_idx][col_idx][0] |= reachable_oceans[row_idx][col_idx-1][0]
            else:
                reachable_oceans[row_idx][col_idx][0] = 1

            # Check North neighbor
            if row_idx - 1 >= 0:
                if current_height >= heights[row_idx-1][col_idx]:
                    reachable_oceans[row_idx][col_idx][0] |= reachable_oceans[row_idx-1][col_idx][0]
            else:
                reachable_oceans[row_idx][col_idx][0] = 1

        # Check reachability to Atlantic Ocean
        for row_idx, col_idx in product(range(num_rows-1, -1, -1), range(num_cols-1, -1, -1)):
            current_height = heights[row_idx][col_idx]
            # Check East neighbor
            if col_idx + 1 < num_cols:
                if current_height >= heights[row_idx][col_idx+1]:
                    reachable_oceans[row_idx][col_idx][1] |= reachable_oceans[row_idx][col_idx+1][1]
            else:
                reachable_oceans[row_idx][col_idx][1] = 1

            # Check South neighbor
            if row_idx + 1 < num_rows:
                if current_height >= heights[row_idx+1][col_idx]:
                    reachable_oceans[row_idx][col_idx][1] |= reachable_oceans[row_idx+1][col_idx][1]
            else:
                reachable_oceans[row_idx][col_idx][1] = 1

        result = []
        for row_idx, col_idx in product(range(num_rows), range(num_cols)):
            bool_oceans = reachable_oceans[row_idx][col_idx]
            if bool_oceans[0] and bool_oceans[1]:
                result.append([row_idx, col_idx])

        return result


def main():
    print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))


if __name__ == "__main__":
    main()
