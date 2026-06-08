class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        
        def dfs(a: int, b: int, index: int) -> bool:
            curr = sum(nums[index: ])
            if a > b + curr or b > a + curr:
                return False
            if index == len(nums):
                return a == b
            
            return dfs(a + nums[index], b, index + 1) or dfs(a, b + nums[index], index + 1)
        
        return dfs(0, 0, 0)


