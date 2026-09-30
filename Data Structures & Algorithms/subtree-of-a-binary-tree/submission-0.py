# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #edge cases: no tree 
        #no sub tree, then its obviously true 

        #check if the subroot starts with root, then compare, if not search through left and right 
        def sameTree(p, q):
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            same_left = sameTree(p.left, q.left)
            same_right = sameTree(p.right, q.right)

            return same_left and same_right

        if subRoot is None:
            return True 

        if root is None:
            return False

        if sameTree(root, subRoot):
            return True

        return(
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )

        



        