class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=[]
        s=s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                p.append(s[i])
        l=0
        r=len(p)-1
        while l<r:
            
            if p[l]!=p[r]:
                return False
            l=l+1
            r=r-1
        
        return True

            