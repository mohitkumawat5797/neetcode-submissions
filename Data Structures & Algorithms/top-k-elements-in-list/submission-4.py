class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
            #count[num] is value stored in dictionary
            #           for key num
        
        array = []
        for key,value in count.items():
            array.append([value,key])
        array.sort()

        result = [] 
        while len(result) < k :
            result.append(array.pop()[1])
        return result
