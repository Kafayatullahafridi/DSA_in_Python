
##time complexity O(n)
prices = [ 7,5,6,4,23]

def findMaxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] <min_price:
            min_price =prices[i]
        elif prices[i] -min_price >max_profit:
            max_profit = prices[i]- min_price
    return max_profit








maxProfit = findMaxProfit(prices)
print(maxProfit)