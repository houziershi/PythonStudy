# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        # root node
        middle = len(nums) // 2
        node = TreeNode(nums[middle])
        if middle == 0:
            node.left = TreeNode(nums[0])
            return node

        if middle

        node.left = TreeNode(nums[middle // 2])
