class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if(l<=1):
            return l
        d = {}
        count = i = ans = 0
        while(i<l):
            if(s[i] not in d):
                d[s[i]] = i
                count +=1
                i+=1
            else:
                i = d[s[i]] +1
                if count>ans:
                    ans = count
                count = 0
                d = {}
        if(count>ans):
            ans = count
        return ans
