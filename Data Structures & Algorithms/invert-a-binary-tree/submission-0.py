# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #whats binary tree
        #how to invert 

        #edge cases: no root/ no tree 

        #using a helper function so we can use recursive technique 
        def invert(root):
            if not root:
                return 

            #swapping the values of left and right child 
            root.left, root.right = root.right, root.left 

            #calling the invert function for doing the same with left child of the root and later right child 
            invert(root.left)
            invert(root.right)

        #calling the helper function
        invert(root)

        return root
        