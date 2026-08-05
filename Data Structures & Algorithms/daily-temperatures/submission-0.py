class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for i in range (len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                p=stack.pop()
                result[p]=i-p
            stack.append(i)
        return result

        