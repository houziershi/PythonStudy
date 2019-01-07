#!usr/bin/env python3
# -*- coding: utf-8 -*-
from DataStructureAndAlgorithm.tree import Tree


class BinaryTree(Tree):
    def left(self, p):
        """Return the position that represents the left child of p, or None if p has no left child"""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return the position that represents the right child of p, or None if p has no right child."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return the position that represents the sibling of p, or None if p has no sibling."""
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)

        if p == self.right(parent):
            return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        elif self.right(p) is not None:
            yield self.right(p)

    #override inherited verison to make inorder the default
    def positions(self):
        return self.inorder()

    def inorder(self):
        """Generate and iteration of Positinos in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate a inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for left_position in self._subtree_inorder(self.left(p)):
                yield left_position

        yield p
        if self.right(p) is not None:
            for right_position in self._subtree_inorder(self.right(p)):
                yield right_position






