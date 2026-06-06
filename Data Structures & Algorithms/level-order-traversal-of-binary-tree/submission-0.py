# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        tree = [root]
        ans = []

        while tree:
            curr_level = []
            for _ in range(len(tree)):
                curr = tree.pop(0)

                curr_level.append(curr.val)

                if curr.left:
                    tree.append(curr.left)
                if curr.right:
                    tree.append(curr.right)
            ans.append(curr_level)

        return ans
            

            


        