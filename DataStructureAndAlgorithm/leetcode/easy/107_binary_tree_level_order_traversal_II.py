# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom2(self, root: TreeNode):
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current = next_level
            result.append(vals)

        return result[::-1]

    def levelOrderBottom3(self, root: TreeNode):
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current = next_level
            result.insert(0, vals)

        return result

    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        else:
            q = collections.deque()
            q.append(root)
            head = root
            tail = root
            result = []
            sub = []
            while len(q) > 0:
                node = q.pop()

                if node == head and node == tail:
                    sub = []
                    sub.append(node.val)
                    result.insert(0, sub)
                elif node == head:
                    sub = []
                    sub.append(node.val)
                elif node == tail:
                    sub.append(node.val)
                    result.insert(0, sub)
                else:
                    sub.append(node.val)

                if node.left is not None:
                    q.appendleft(node.left)

                if node.right is not None:
                    q.appendleft(node.right)

                if head is None:
                    if node.left:
                        head = node.left
                    elif node.right:
                        head = node.right
                elif node == head:
                    if node.left:
                        head = node.left
                    elif node.right:
                        head = node.right
                    else:
                        head = None

                if tail is None:
                    if node.right:
                        tail = node.right
                    elif node.left:
                        tail = node.left
                elif node == tail:
                    if node.right:
                        tail = node.right
                    elif node.left:
                        tail = node.left
                    else:
                        tail = head

            return result


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(4)
    node5 = TreeNode(8)
    # node6 = TreeNode(15)
    # node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    # node3.left = node6
    # node3.right = node7

    Solution().levelOrderBottom3(node1)

    a = [2]
    a.insert(0, 5)
    a.insert(0, 4)
    print(a)

    """
        Time Complexity = ?
        Space Complexity = ?
        Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
        For example:
        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        return its level order traversal as:
        [
          [3],
          [9,20],
          [15,7]
        ]   
    """
