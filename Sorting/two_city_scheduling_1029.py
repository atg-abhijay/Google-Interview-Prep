"""
URL of problem:
https://leetcode.com/problems/two-city-scheduling/
"""


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = int(len(costs) / 2)
        min_costs = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
        min_costs[0][0] = 0
        for idx, [cost_a, cost_b] in enumerate(costs):
            idx += 1
            for row_idx, col_idx in zip(range(idx+1), range(idx, -1, -1)):
                if not (0 <= row_idx <= n and 0 <= col_idx <= n):
                    continue

                north_x = row_idx - 1
                lowest_value = min_costs[row_idx][col_idx]
                if north_x >= 0:
                    lowest_value = min(min_costs[north_x][col_idx] + cost_b, lowest_value)

                west_y = col_idx - 1
                if west_y >= 0:
                    lowest_value = min(min_costs[row_idx][west_y] + cost_a, lowest_value)

                min_costs[row_idx][col_idx] = lowest_value

        return min_costs[n][n]


def main():
    print(
        Solution().twoCitySchedCost(
            [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
        )
    )


if __name__ == "__main__":
    main()
