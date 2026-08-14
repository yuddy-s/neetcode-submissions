class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1

        # [1, 3, 5, 7, 9] // t = 12

        while True:
            if numbers[index1] + numbers[index2] == target:
                return [index1+1, index2+1]
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
                continue

            index2 -= 1


        return [index1+1, index2+1]