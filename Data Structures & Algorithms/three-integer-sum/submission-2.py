class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        length = len(nums)
        j, k = 1, length - 1
        nums.sort()

        # print(nums)

        if length == 3:
            if (nums[0] + nums[1] + nums[2]) == 0:
                return [[nums[0], nums[1], nums[2]]] 
            else:
                return []

        for i in range(0, length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # print("new")
            j = i + 1
            k = length - 1
            while j < k:
                # print(i, j, k)
                # print(nums[i], nums[j], nums[k])
                # print("=")
                if nums[j] + nums[k] == -(nums[i]):
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # skip duplicate j values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif nums[j] + nums[k] > -(nums[i]):
                    k -= 1
                else:
                    j += 1

                if j >= k:
                    break


        return result


