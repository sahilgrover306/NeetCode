class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a = sorted(d.items(), key=lambda x: x[1], reverse=True)
        ans = []
        count = 0
        for i in a:
            if count == k:
                return ans
            count+=1
            ans.append(i[0])
        return ans
