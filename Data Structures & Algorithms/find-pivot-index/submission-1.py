class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)):
            current = nums[i]
            left = 0
            right = 0

            for j in range(i, len(nums)):
                right += nums[j]
            
            for j in range(i, -1, -1):
                left += nums[j]
            
            if left == right:
                return i


        return -1
            


        

