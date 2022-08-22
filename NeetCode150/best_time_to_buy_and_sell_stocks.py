class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        ans = 0
        if(l<=1):
            return 0
        i = 0
        j = 1
        while(j<l):
            if(prices[i]>prices[j]):
                i = j
                j+=1
            else:
                if (prices[j]-prices[i])>ans:
                    ans = prices[j]-prices[i]
                j+=1
        return ans
