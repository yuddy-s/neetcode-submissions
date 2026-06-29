class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency = {}
        count = 0

        for num in nums:
            if num not in frequency:
                frequency.update({num: 1})
            else:
                frequency[num] += 1
        print(frequency)
        while count < k:
            max = 0 # max value found
            index = 0 # key/index of max value found
            for key, val in frequency.items():
                if val > max:
                    max = val
                    index = key
            
            result.append(index)
            frequency.pop(index)
            count += 1
        
        return result
