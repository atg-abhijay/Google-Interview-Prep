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
        """
        Time Limit Exceeded with this solution
        """
        upper_limit, num_coins = float('inf'), len(coins)
        least_coins = [[upper_limit] * (amount + 1) for _ in range(num_coins + 1)]
        for row in least_coins:
            row[0] = 0

        for amt, item_idx in product(range(1, amount+1), range(1, num_coins+1)):
            coin_val = coins[item_idx-1]
            if coin_val > amt:
                least_coins[item_idx][amt] = least_coins[item_idx - 1][amt]
            else:
                max_quantity = int(amt / coin_val)
                generate_num_coins = lambda q: q + least_coins[item_idx - 1][amt - q * coin_val]
                least_coins[item_idx][amt] = min(
                    least_coins[item_idx - 1][amt],
                    *[generate_num_coins(q) for q in range(1, max_quantity + 1)]
                )

        output = least_coins[num_coins][amount]
        return -1 if output >= upper_limit else output


def main():
    print(Solution().coinChange([470, 35, 120, 81, 121], 9825))


if __name__ == "__main__":
    main()
