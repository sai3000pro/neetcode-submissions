class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums) # can do nums.sort()
        res = []
        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue # instead of just incrementing by += 1, cleaner
            target = -sortedNums[i]
            j, k = i + 1, len(sortedNums) - 1
            while j < k:
                currSum = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if currSum < 0:
                    j += 1
                elif currSum == 0:
                    res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    # Skip duplicate values for the second and third elements
                    while j < k and sortedNums[j] == sortedNums[j+1]:
                        j += 1
                    while j < k and sortedNums[k] == sortedNums[k-1]:
                        k -= 1
                    # Move both pointers to continue the search. Think about what would happen if those while loops didn't occur
                    j += 1
                    k -= 1
                else:
                    k -= 1
            
        return res