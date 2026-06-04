# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return same_tree(p.left, q.left) and same_tree(p.right, q.right)
        if not root:
            return True
        tree = [root]

        while tree:
            curr = tree.pop()
            if curr.val == subRoot.val:
                if same_tree(curr, subRoot):
                    return True
                
            if curr.left:
                tree.append(curr.left)
            
            if curr.right:
                tree.append(curr.right)
        
        return False