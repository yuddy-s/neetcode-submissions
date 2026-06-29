class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(0, length):
            for j in range (1, length):
                if (nums[i] + nums[j] == target) and i != j:
                    return [i, j]

        return []