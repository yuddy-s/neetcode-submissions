class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(0, len(nums)):
            print(nums)
            if nums[i] == val:
                nums[i] = 999
            else:
                count += 1
        
        nums.sort()
        return count

