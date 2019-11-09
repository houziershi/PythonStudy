# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, l, r):
        if l <= r:
            mid = l + (r - l) // 2
            root = TreeNode(nums[mid])
            root.left = self.helper(nums, l, mid - 1)
            root.right = self.helper(nums, mid + 1, r)
            return root

    def noRecursive(self, nums, l, r):
        pass

    def preOrderTraversal(self, root: TreeNode):
        print(root.val)
        if root.left is not None:
            self.preOrderTraversal(root.left)

        if root.right is not None:
            self.preOrderTraversal(root.right)


if __name__ == '__main__':
    node = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    Solution().preOrderTraversal(node)
