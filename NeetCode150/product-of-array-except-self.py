class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pref = [0]*l
        post = [0]*l
        output = [0]*l
        pref[0] = nums[0]
        for i in range(1,l):
            pref[i] = pref[i-1]*nums[i]
        post[l-1] = nums[l-1]
        for i in range(1,l):
            post[l-i-1] = post[l-i]*nums[l-i-1]
        output[0] = post[1]
        output[l-1] = pref[l-2]
        for i in range(1,l-1):
            output[i] = pref[i-1] * post[i+1]
        return output
