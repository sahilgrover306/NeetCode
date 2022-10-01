class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = len(h)
        left = 0
        right = l-1
        ans = 0
        while(left<right):
            temp = min(h[left],h[right])*(right-left)
            if(ans<temp):
                ans = temp
            if(h[left]<h[right]):
                left+=1
            else:
                right-=1
        return ans
