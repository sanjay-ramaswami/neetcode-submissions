class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=[]
        r=[]
        s=s.lower()
        s=s.replace(" ","")
        for i in range(len(s)):
            if s[i].isalnum():
                r.append(s[i])
        
        
        for i in range(len(r)-1,-1,-1):
            p.append(r[i])
        if r==p:
            return True
        return False