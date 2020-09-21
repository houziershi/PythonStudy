# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            return self.helper(root.left, -sys.maxsize - 1, root.val) and self.helper(root.right, root.val, sys.maxsize)
        else:
            return True

    def helper(self, node: TreeNode, lower_limit, upper_limit) -> bool:
        if node:
            if upper_limit > node.val > lower_limit:
                return self.helper(node.left, lower_limit, node.val) and self.helper(node.right, node.val, upper_limit)
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(5)
    node4 = TreeNode(0)
    node5 = TreeNode(2)
    node6 = TreeNode(3)
    node7 = TreeNode(4)
    node8 = TreeNode(6)

    # 3 1 5
    node1.left = node2
    node1.right = node3
    # 1 0 2
    node2.left = node4
    node2.right = node5

    # 2   3
    node5.right = node6
    # 5 4 6
    node3.left = node7
    node3.right = node8

    print(Solution().isValidBST(node1))
