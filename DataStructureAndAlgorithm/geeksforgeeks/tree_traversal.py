# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# A function to do inorder tree traversal without recursion
def printInorder2(root: Node):
    stack = [root]
    current = root.left
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            temp = stack.pop()
            print("inorder2 ", temp.val)
            current = temp.right
        else:
            break


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# A function to do Preorder tree traversal without recursion
def printPreorder2(root: Node):
    stack = [root]
    current = root.left
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            temp = stack.pop()
            print("Preorder2 ", temp.val)
            current = temp.right
        else:
            break


# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # print("Preorder traversal of binary tree is")
    # printPreorder(root)
    #
    print("Inorder traversal of binary tree is")
    printInorder2(root)
    #
    # print("Postorder traversal of binary tree is")
    # printPostorder(root)
