class Solution:
    def trap(self, height: List[int]) -> int:
        if not height :
            return 0
        n = len(height)
        
        total_water = 0

        for i in range(n):
            
            leftmax = height[i]
            rightmax = height[i]

            for j in range(i):
                leftmax = max(leftmax , height[j])
            
            for j in range(i+1 , n):
                rightmax = max(rightmax , height[j])
            
            water = min(leftmax,rightmax)
            trapped_water = water - height[i]
            total_water += trapped_water
        
        return total_water
























