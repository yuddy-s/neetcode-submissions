class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curmap = set()
        result = 0
        current = 1

        for num in nums:
            if num not in curmap:
                curmap.add(num)
            else:
                continue
        
        for num in curmap:
            temp = 1
            if num - 1 not in curmap:
                while True:
                    if num + current in curmap:
                        temp += 1
                        current += 1
                    else: 
                        break
            if temp > result:
                result = temp
            current = 1
        
        return result

            
