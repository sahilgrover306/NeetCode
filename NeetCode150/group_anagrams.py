def tostring(l: List[int])-> str:
        s = ""
        for i in l:
            s = s + str(i) + "-"
        return s
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict([])
        for s in strs:
            a = [0]*26
            for i in s:
                a[ord(i)-ord('a')] +=1
            t = tostring(a)
            if t not in d:
                d[t] = []
            d[t].append(s)
        return d.values()
        
