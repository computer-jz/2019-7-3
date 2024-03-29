# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        else:
            lep = self.maxDepth(root.left)
            rep = self.maxDepth(root.right)
        return max(lep,rep)+1