"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
    """
    buy = 0
    sell = len(prices) - 1

    while buy < sell:
        if prices[buy] > prices[sell]:
            sell -= 1
            prices.pop(buy)
        elif prices[buy] > min(prices):
            sell -= 1
            prices.pop(buy)
        elif prices[buy] < prices[sell]:
            return max(prices) - prices[buy]
        else:
            break
    return 0

def maxProfitv2(prices: List[int]) -> int:
    buy, sell, maxprofit = 0, 1, 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit)
        else:
            buy = sell
        sell += 1
    return maxprofit


# print(maxProfit(prices = [7,1,5,3,6,4]))
# print(maxProfitv2(prices = [7,1,5,3,6,4]))
# print(maxProfit(prices = [7,6,4,3,1]))
print(maxProfitv2(prices = [7,6,4,3,1]))
# print(maxProfit(prices = [2,1,4]))
print(maxProfitv2(prices = [2,1,4]))
