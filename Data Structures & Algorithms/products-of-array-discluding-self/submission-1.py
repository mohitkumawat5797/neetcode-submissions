class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [0]*n    # an array like this[0,0,0,-- upto n]

        for i in range(n):
            product = 1
            for j in range(n):
                if i==j :
                    continue
                product = product * nums[j]  # nums[j] means element at index j in list nums
            
            result[i] = product
        return result