class Solution:

    def encode(self, strs: List[str]) -> str:
        en=""
        for i in strs:
            en=en+str(len(i))+'#'+i
        return en

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i<len(s):
            j=i
            while(s[j]!='#'):
                j=j+1
            d=int(s[i:j])
            l.append(s[j+1:d+j+1])
            i=j+d+1

        return l


        
            

            
        
        

