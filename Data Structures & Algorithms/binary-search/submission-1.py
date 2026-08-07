class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        for i in range(len(nums)):
            mid=(l+r)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                l=l+1
            elif target<nums[mid]:
                r=r-1
        return -1