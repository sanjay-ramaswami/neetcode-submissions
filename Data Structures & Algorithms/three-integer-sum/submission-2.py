class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[r]+nums[l]
                if total==0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l=l+1
                    r=r-1
                elif total<0:
                    l=l+1
                elif total>0:
                    r=r-1
        return [list(x) for x in ans]
