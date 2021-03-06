"""
URL of problem:
https://leetcode.com/problems/coin-change/
"""


from itertools import product


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        least_coins = [0] + [float('inf')] * amount
        for amt, coin in product(range(1, amount+1), coins):
            if amt - coin >= 0:
                least_coins[amt] = min(least_coins[amt], least_coins[amt - coin] + 1)

        output = least_coins[-1]
        return -1 if output == float('inf') else output


    def coinChange2(self, coins, amount):
        upper_limit, num_coins = float('inf'), len(coins)
        least_coins = [[upper_limit] * (amount + 1) for _ in range(num_coins + 1)]
        for row in least_coins:
            row[0] = 0

        for amt, item_idx in product(range(1, amount+1), range(1, num_coins+1)):
            coin_val = coins[item_idx-1]
            if coin_val > amt:
                least_coins[item_idx][amt] = least_coins[item_idx - 1][amt]
            else:
                least_coins[item_idx][amt] = min(
                    least_coins[item_idx - 1][amt],
                    least_coins[item_idx][amt - coin_val] + 1
                )

        output = least_coins[num_coins][amount]
        return -1 if output >= upper_limit else output


    def coinChange_2ndPass(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Let there be n coins.
        # Time: O(amount * n), Space: O(amount)
        # Tags: Dynamic Programming
        if amount == 0:
            return 0

        fewest = [0]
        for change in range(1, amount + 1):
            min_coins = float('inf')
            for coin in coins:
                if change - coin >= 0:
                    min_coins = min(min_coins, 1 + fewest[change - coin])

            fewest.append(min_coins)

        if fewest[amount] == float('inf'):
            return -1

        return fewest[amount]


def main():
    print(Solution().coinChange([470, 35, 120, 81, 121], 9825))


if __name__ == "__main__":
    main()
