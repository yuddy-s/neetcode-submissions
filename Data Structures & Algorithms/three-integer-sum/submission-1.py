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
            # print("new")
            j = i + 1
            k = length - 1
            while True:
                # print(i, j, k)
                # print(nums[i], nums[j], nums[k])
                # print("=")
                if nums[j] + nums[k] == -(nums[i]):
                    sort = [nums[i], nums[j], nums[k]]
                    if sort not in result:
                        result.append(sort)
                    j += 1
                elif nums[j] + nums[k] > -(nums[i]):
                    k -= 1
                else:
                    j += 1

                if j >= k:
                    break


        return result


