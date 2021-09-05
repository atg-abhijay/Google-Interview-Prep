"""
URL of problem:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cost_price = prices[0]
        for stock_price in prices[1:]:
            if stock_price <= cost_price:
                cost_price = stock_price
            elif stock_price - cost_price > profit:
                profit = stock_price - cost_price

        return profit

def main():
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == "__main__":
    main()
