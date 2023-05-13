class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

solution = Solution()

list = [2, 7, 11, 15]

result = solution.maxProfit(list)
print(result)  # Output: [0, 1]

def maxProfit(prices):
	    l, r = 0, 1
	    maxP = 0

	    while r < len(prices):
	        if prices[l] < prices[r]:
	            profit = prices[r] - prices[l]
	            maxP = max(maxP, profit)
	        else:
                 l = r
	        r += 1

	    return maxP

prices = [22,43,4, 7, 11, 15]
result = maxProfit(prices)
print(result)  # Output: 13