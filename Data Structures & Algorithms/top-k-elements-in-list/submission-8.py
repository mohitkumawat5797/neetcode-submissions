class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num , 0) + 1
        
        arr = []
        for key,value in count.items():
            arr.append([value,key])
        arr.sort()

        arr = arr[-k:]
        return [item[1] for item in arr]