class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = float('-inf')
        sold = 0
        rest = 0

        for price in prices:

            old_hold = hold
            old_sold = sold
            old_rest = rest

            hold = max(old_hold, old_rest - price)

            sold = old_hold + price

            rest = max(old_rest, old_sold)

        return max(sold, rest)