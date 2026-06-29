class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        l = len(nums)

        for i in range(0, l): 
            if nums[i] not in seen:
                seen.append(nums[i])
            elif nums[i] in seen:
                return True
        
        return False