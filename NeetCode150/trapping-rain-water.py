class Solution:
    def trap(self, h: List[int]) -> int:
        l = len(h)
        if(l<0):
            return 0
        i = 0
        j = l - 1
        l = h[i]
        r = h[j]
        ans = 0
        while(i<j):
            if(l<r):
                i +=1
                l = max(l,h[i])
                ans += l - h[i]
                
            else:
                j-=1
                r = max(r,h[j])
                ans += r - h[j]
                
        return ans
        
