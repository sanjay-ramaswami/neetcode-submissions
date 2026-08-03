class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"}":"{",
            "]":"[",
            ")":"("}
        for char in s:
            if  char in "{[(" :
                stack.append(char)
            elif char in "}])":
                if len(stack)!=0:
                    top=stack[-1]
                    if top == d[char]:
                        stack.pop()
                    else:
                        return False
                elif len(stack)==0:
                    return False
                
                
                
        return len(stack)==0
               

                
            
      



                

        