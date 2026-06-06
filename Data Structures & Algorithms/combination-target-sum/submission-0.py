class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        curr_set = []
        ans = []
        def dfs(curr_sum, index):
            if curr_sum > target:
                return
            if index == len(nums):
                if curr_sum == target:
                    ans.append(curr_set.copy())
                return

            curr_set.append(nums[index])
            dfs(curr_sum + nums[index], index)

            curr_set.pop()
            dfs(curr_sum, index + 1)
        
        dfs(0, 0)
        return ans
        