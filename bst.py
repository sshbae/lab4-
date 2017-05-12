#a bst is one of
# - None
# - a bst

class bstNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == bstNode)
          and self.value == other.value
          and self.left == other.left
          and self.right == other.right)

    def __repr__(self):
        return ("bstNode({!r}, {!r}, {!r})".format(self.value, self.left, self.right))

class BinarySearchTree:
    def __init__(self, comes_before, bst):
        self.comes_before = comes_before
        self.bst = bst
    def __eq__(self, other):
        return ((type(other) == BinarySearchTree)
          and self.comes_before == other.comes_before
          and self.bst == other.bst)
    def __repr__(self):
        return ("BinarySearchTree({!r}, {!r})".format(self.comes_before, self.bst))

def is_empty(tree):
    if tree.bst is None:
        return True
    return False

def insert(tree, value):
    if tree.bst is None:
        return BinarySearchTree(tree.comes_before, bstNode(value, None, None))
    if comes_before(value, bst.value):
        return BinarySearchTree(tree.comes_before, bstNode(tree.bst.value, insert(BinarySearchTree(tree.comes_before, tree.bst.left), value), tree.bst.right))
    if comes_before(bst.value, value):
        return BinarySearchTree(tree.comes_before, bstNode(tree.bst.value, tree.bst.left, insert(BinarySearchTree(tree.comes_before, tree.bst.right), value)))
    return tree

