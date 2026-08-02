class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        p=1
        for i in range(len(nums)):
            p=1
            for j in range(len(nums)):
                if i !=j:
                    p=p*nums[j]
            out.append(p)

            
        return out

        