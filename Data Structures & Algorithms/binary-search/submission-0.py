class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1   # indexes

        while start <= end:
            mid = (start+end)//2       # index

            if target == nums[mid]:
                return mid
            
            elif target < nums[mid]:
                end = mid - 1
            
            else :
                start = mid + 1
        return -1
          








