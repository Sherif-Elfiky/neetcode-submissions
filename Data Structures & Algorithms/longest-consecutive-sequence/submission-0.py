class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        globalMax = 0


        for n in nums:

            if n - 1 in numSet:
                continue
            
            localMax = 1
            while n + 1 in numSet:
                n += 1
                localMax += 1
            globalMax = max(localMax, globalMax)
        return globalMax


            
        