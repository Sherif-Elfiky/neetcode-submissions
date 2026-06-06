class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        indices = {}

        for i, n in enumerate(nums):

            want = target - n

            if want in indices:
                return [indices[want], i]
            
            indices[n] = i
        return [-1, -1]
        