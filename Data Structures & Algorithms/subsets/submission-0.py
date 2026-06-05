class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        curr_list = []
        ans = []

        def helper(index):
            if index == len(nums):
                ans.append(curr_list.copy())
                return


            curr_list.append(nums[index])
            helper(index + 1)
            curr_list.pop()
            helper(index + 1)
       


        helper(0)
        return ans
        

        