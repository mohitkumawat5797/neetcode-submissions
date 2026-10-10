class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        res_area = 0

        while left<right :
            height = min(heights[left],heights[right])
            width = right - left
            curr_area = height * width
            if curr_area > res_area :
                res_area = curr_area
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return res_area