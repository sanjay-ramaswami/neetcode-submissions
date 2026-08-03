class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(numbers):
            x=target-numbers[i]
            if x in d:
                return [d[x]+1,i+1]
            d[num]=i
                
        