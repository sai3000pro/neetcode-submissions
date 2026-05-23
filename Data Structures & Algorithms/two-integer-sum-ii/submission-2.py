class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        res = []
        while True:
            curr = numbers[index1] + numbers[index2]
            if curr > target:
                index2 = index2 - 1
            elif curr < target:
                index1 = index1 + 1
            else:
                break

        res.append(index1 + 1)
        res.append(index2 + 1)
        return res