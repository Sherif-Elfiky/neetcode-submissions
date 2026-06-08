# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        tree = [root]
        right_side = []

        while tree:
            for _ in range(len(tree)):
                curr = tree.pop(0)

                if curr.left:
                    tree.append(curr.left)
                if curr.right:
                    tree.append(curr.right)
            right_side.append(curr.val)
        return right_side
        