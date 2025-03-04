"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""
from typing import Optional

from DataStructures.BinaryTreev2 import Node


def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    def preorder_print(root: Node, traversal: str = ''):
        if root:
            traversal += (str(root.value) + '-')
            traversal = preorder_print(root.left, traversal)
            traversal = preorder_print(root.right, traversal)
        return traversal

    if preorder_print(p) == preorder_print(q):
        return True
    return False

def isSameTreev2(p: Optional[Node], q: Optional[Node]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.value != q.value:
        return False

    node1 = isSameTreev2(p.left, q.left)
    node2 = isSameTreev2(p.right, q.right)

    if node1 and node2:
        return True
    return False
    # return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))





tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)

tree2 = Node(1)
tree2.left = Node(2)
tree2.right = Node(3)

print(isSameTree(p=tree1, q=tree2))
print(isSameTreev2(p=tree1, q=tree2))


