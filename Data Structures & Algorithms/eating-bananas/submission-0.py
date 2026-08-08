class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        high=max(piles)
        while l<=high:
            mid=(l+high)//2
            hour=0
            for p in piles:
                hour+=(p+mid-1)//mid
            if hour<=h:
                high=mid-1
            else:
                l=mid+1
        return l
        