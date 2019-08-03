# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        else:
            return self.isSameTree(root.left, root.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

    """
        Time Complexity = O(N^2)
        Space Complexity = O(1)
        Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
        For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
        Example:
            1
           / \
          2   2
         / \ / \
        3  4 4  3
    """
