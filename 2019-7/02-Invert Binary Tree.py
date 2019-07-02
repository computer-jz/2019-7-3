
 class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
       # root.left, root.right = root.right, root.left
        root1=root.left
        root.left=root.right
        root.right=root1
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root