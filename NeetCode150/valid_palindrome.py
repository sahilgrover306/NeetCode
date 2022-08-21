class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while(i<j):
            if s[i].isalnum() == False:
                i += 1
            elif s[j].isalnum() == False:
                j -= 1
            else:
                if s[i]!=s[j]:
                    return False
                i += 1
                j -= 1
        return True
