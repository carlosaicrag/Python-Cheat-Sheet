def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def numberLessThanCurrent(lookAheadInt, currentNum):
            if lookAheadInt == len(prices):
                return True
            elif prices[lookAheadInt] < currentNum:
                return True
            else:
                return False

        totalProfit = 0
        tempProfit = 0
        buy = prices[0]

        for idx in range(len(prices)):
            if idx + 1 == len(prices):
                totalProfit += tempProfit
                break

            if numberLessThanCurrent(idx+1, prices[idx]):
                totalProfit += tempProfit
                tempProfit = 0
                buy = prices[idx+1]
            elif numberLessThanCurrent(idx+1, buy):
                totalProfit += tempProfit
                tempProfit = 0
                buy = prices[idx+1]
            else:
                tempProfit = (prices[idx+1] - buy)

        return totalProfit

print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([1,2,3,4,5]))