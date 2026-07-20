class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0
        #prices=[7,1,5,3,6,4]

        for i in range(1,len(prices)):
            best = max(best,prices[i] - prices[l])
            if prices[l] > prices[i]:
                l = i
        return best
        
        