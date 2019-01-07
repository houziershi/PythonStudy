#!usr/bin/env python3
# -*- coding: utf-8 -*-
from DataStructureAndAlgorithm.linked_queue import LinkedQueue


class Tree:
    class Position:
        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        """Return the position of the root of tree T, or None if T is empty."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return the position of the parent of position p,or None if p is the root of T."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children of position p."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of the children of position p."""
        raise NotImplementedError('must be implemented by subclass')

    def positions(self):
        """Generate an iteration of all positions of tree T."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------

    def is_root(self, p):
        """Return True if position p is the root of Tree T."""
        return self.root() == p

    def is_empty(self):
        """Return True if tree T does not contain any positions."""
        return len(self) == 0

    def is_leaf(self, p):
        """Return True if position p does not have any children."""
        return self.num_children(p) == 0

    def depth(self, p):
        """:return int Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height1(self):  # works, but O(n^2) worst-case time
        """:return Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def height2(self, p):
        """Return the height of the subtree rooted at Position p."""

        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height2(q) for q in self.children(p))

    def height(self, p=None):
        """
        Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree.
        :param p:
        :return:
        """
        if p is None:
            p = self.root()
        return self.height2(p)

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            tree_list = LinkedQueue()
            tree_list.enqueue(self.root())
            while not tree_list.is_empty():
                p = tree_list.dequeue()
                yield p
                for c in self.children(p):
                    tree_list.enqueue(c)
