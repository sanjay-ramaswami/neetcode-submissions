class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lmax,rmax=0,0
        water=0
        while l<r:
            if height[l]<height[r]:
                lmax=max(height[l],lmax)
            
                water=water+(lmax-height[l])
                l=l+1
            else:
                rmax=max(rmax,height[r])
                water+=(rmax-height[r])
                r=r-1
        return water
