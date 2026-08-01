class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=set()
        n=len(nums)
        l=set(nums)
        if(n!=len(l)):
            return True
        return False