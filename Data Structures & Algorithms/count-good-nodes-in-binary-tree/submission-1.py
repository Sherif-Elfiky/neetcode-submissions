# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


       

        def dfs(node, maxi):
            
          

            if not node:
                return 0

            ans = 0

            if node.val >= maxi:
                ans += 1

            maxi = max(maxi, node.val)

            return ans + dfs(node.left, maxi) + dfs(node.right, maxi)
        return dfs(root, float('-inf'))



        