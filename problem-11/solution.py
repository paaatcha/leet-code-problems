# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def tree_depth (root):

            if root is None:
                return 0

            return max(tree_depth(root.left), tree_depth(root.right)) + 1
        
        
        def diameter (root):
            
            if root is None:
                return 0
            
            depth_left = tree_depth (root.left)
            depth_right = tree_depth (root.right)
            
            lef_dia = diameter (root.left)
            righ_dia = diameter (root.right)
            
            return max(depth_left + depth_right, max(lef_dia, righ_dia))
            
            
        return diameter(root)


        
        
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    sol = Solution()
    ans = sol.diameterOfBinaryTree(root)

    print(ans)
    