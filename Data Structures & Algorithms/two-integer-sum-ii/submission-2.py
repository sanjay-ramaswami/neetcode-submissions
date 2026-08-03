class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            x=target-numbers[l]
            if x==numbers[r]:
                return [l+1,r+1]
            elif x<numbers[r]:
                r=r-1
            elif x>numbers[r]:
                l=l+1
            


                
        