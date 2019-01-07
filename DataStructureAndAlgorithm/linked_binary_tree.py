#!usr/bin/env python3
# -*- coding: utf-8 -*-
from DataStructureAndAlgorithm.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, e, parent=None, left=None, right=None):
            self._element = e
            self._parent = parent
            self._right = right
            self._left = left

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and self._node is other._node

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def left(self, p):
        """Return the position that represents the left child of p, or None if p has no left child"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position that represents the right child of p, or None if p has no right child."""
        node = self._validate(p)
        return self._make_position(node._right)

    def root(self):
        """Return the position of the root of tree T, or None if T is empty."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of the parent of position p,or None if p is the root of T."""
        n = self._validate(p)
        return self._make_position(n._parent)

    def _make_position(self, node):
        """:return Position :utility for wrapping a node as a position"""
        return self.Position(self, node) if node is not None else None

    def _validate(self, p):
        """:return Node: utility for robustly checking the validity of a given position instance when unwrapping it"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')

        return p._node

    def num_children(self, p):
        """:return int: Return the position of the parent of position p,or None if p is the root of T."""
        n = self._validate(p)
        i = 0
        if n._left is not None:
            i += 1
        if n._right is not None:
            i += 1
        return i

    # def positions(self):
    #     """:returns Positions: Generate an iteration of all positions of tree T."""
    #     if self.is_empty():
    #         return None
    #     if len(self) == 1:
    #         return self.root()
    #     else:
    #         return self.children(self.root())

    def __len__(self):
        """:return int: Return the total number of elements in the tree."""
        return self._size

        # ---------- add methods in this class ----------

    def add_root(self, e):
        """Create a root for an empty tree, storing e as the element,and return the position
          of that root; an error occurs if the tree is not empty."""
        if self._root is not None:
            raise ValueError('Tree has a root')
        self._size = 1
        self._root = self._Node(e, None, None, None)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """Create a new node storing element e, link the node as the
           left child of position p, and return the resulting position;
           an error occurs if p already has a left child."""
        n = self._validate(p)
        if n._left is not None:
            raise ValueError('Left child exists')
        left_node = self._Node(e, None, None, None)
        n._left = left_node
        left_node._parent = n
        self._size += 1
        return self.Position(self, left_node)

    def add_right(self, p, e):
        """Create a new node storing element e, link the node as the
            right child of position p, and return the resulting position;
            an error occurs if p already has a right child."""
        n = self._validate(p)
        if n._right is not None:
            raise ValueError('Right child exists')
        right_node = LinkedBinaryTree._Node(e, None, None, None)
        n._right = right_node
        right_node._parent = n
        self._size += 1
        return LinkedBinaryTree.Position(self, right_node)

    def replace(self, p, e):
        """Replace the element stored at position p with element e,
           and return the previously stored element."""
        n = self._validate(p)
        answer = n._element
        n._element = e
        return answer

    def delete(self, p):
        """Remove the node at position p, replacing it with its child,
           if any, and return the element that had been stored at p;
           an error occurs if p has two children."""
        node = self._validate(p)
        if self.is_leaf(p):
            parent_node = node._parent
            if parent_node._left == node:
                parent_node._left = None
            else:
                parent_node._right = None
            self._size -= 1
            return node._element

        if self.num_children(p) == 2:
            raise ValueError('p has two children, can not be deleted')

        if node._right is not None:
            parent_node = node._parent  #
            node._right._parent = parent_node
            if parent_node._left == node:
                parent_node._left = node._right
            else:
                parent_node._right = node._right
            self._size -= 1
            return node._element

        if node._left is not None:
            parent_node = node._parent
            node._left._parent = parent_node
            if parent_node._left == node:
                parent_node._left = node._left
            else:
                parent_node._right = node._left
            self._size -= 1
            return node._element

    def attach(self, p, T1, T2):
        """Attach the internal structure of trees T1 and T2, respectively, as the left and right subtrees of leaf position p of
           T, and reset T1 and T2 to empty trees; an error condition
           occurs if p is not a leaf"""
        if self.is_leaf(p):

            if not type(self) is type(T1) is type(T2):
                raise TypeError('Tree types must match')

            p_node = self._validate(p)  # p node

            if not T1.is_empty():
                p_node._left = T1._root
                T1._root._parent = p_node
                self._size += T1._size

                T1._root = None
                T1._size = 0

            if not T2.is_empty():
                p_node._right = T2._root
                T2._root._parent = p_node
                self._size += T2._size

                T2._root = None
                T2._size = 0

        else:
            raise ValueError('p is not a leaf, can not attach')


if __name__ == '__main__':
    binaryTree = LinkedBinaryTree()
    binaryTree.add_root(45)
