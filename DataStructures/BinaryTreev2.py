from typing import Any, List, Optional
from collections import deque


class Node(object):
    def __init__(self, value=1, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree(object):
    """
    Usage:
        tree = BinaryTree(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
    """

    def __init__(self, root: Node | Any) -> None:
        self.root = Node(root)

    def __str__(self) -> str:
        return str(self.root)

    def print_tree(self, traversal_type: str = 'preorder'):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, '')

    def preorder_print(self, root: Node, traversal: str = ''):
        if root:
            traversal += (str(root.value) + '-')
            traversal = self.preorder_print(root.left, traversal)
            traversal = self.preorder_print(root.right, traversal)
        return traversal

    def preorder_iterative(self, root: Node):
        if root is None:
            return None

        nodes = []
        result = []
        nodes.append(root)

        while len(nodes) > 0:
            node = nodes.pop()
            result.append(node.value)
            # print(node.value, '-')

            if node.right is not None:
                nodes.append(node.right)
            if node.left is not None:
                nodes.append(node.left)
        return result

    def inorder_print(self, root: Node, traversal: str):
        if root:
            traversal = self.inorder_print(root.left, traversal)
            traversal += (str(root.value) + '-')
            traversal = self.inorder_print(root.right, traversal)
        return traversal

    def invert_tree_r(self, root: Node):
        if root:
            # root.left, root.right = self.invert_tree_r(root.right), self.invert_tree_r(root.left)
            temp = self.invert_tree_r(root.left)
            root.left = self.invert_tree_r(root.right)
            root.right = temp
            return root

    def invert_tree_q(self, root: Node):
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root

    def diameter(self, root: Node):
        result = [0]

        def dfs(root):
            if not root:
                return -1

            left_node = dfs(root.left)
            right_node = dfs(root.right)
            result[0] = max(result[0], 2 + left_node + right_node)

            return 1 + max(left_node, right_node)

        dfs(root)
        return result[0]


    def max_depth(self, root: Node):
        if not root:
            return 0

        left_node = self.max_depth(root.left)
        right_node = self.max_depth(root.right)
        node_depth = 1 + max(left_node, right_node)
        return node_depth

    def height_tree(self, root: Node):
        ...

    def size_tree(self):
        if self.root is None:
            return 0

        size = 1
        stack = []
        stack.append(self.root)

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                size += 1
            if node.right:
                stack.append(node.right)
                size += 1
        return size


    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        result, nodes_q = [], []
        nodes_q.append(root)

        while len(nodes_q) > 0:
            if node := nodes_q.pop(0):
                result.append([node.value])
                nodes_q.append(node.left)
                nodes_q.append(node.right)
            if node is None:
                result.append([None])

        for l in result:
            if l[0] is None:
                result.remove(l)

        nodes_l = len(result)
        c1, c2, = 1, 2
        while c2 < nodes_l + 1:
            result[c1] = result[c1] + result[c2]
            result.pop(c2)
            c1 += 1
            c2 += 1

        return result[:nodes_l]

    def isSymmetric(self, root: Optional[Node]) -> bool:
        nodes, nodes_r, nodes_l = [], [], []
        nodes.append(root)

        while nodes:
            if node := nodes.pop(0):
                nodes.append(node.left)
                nodes.append(node.right)

                nodes_l.append(node.left)
                nodes_r.append(node.right)

        if nodes_l == nodes_r:
            return True
        return False



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.right.left = Node(4)
tree.root.right.left = Node(3)
# tree.root.left.right.left = Node(5)
# tree.root.left.right.right = Node(6)

# print(tree.preorder_print(tree.root, ''))
# tree.inorder_print(tree.root, '')
# print(tree.invert_tree_r(tree.root))
# print(tree.preorder_print(tree.root, ''))
# print(tree.diameter(tree.root))
# print(tree.max_depth(tree.root))
# print(tree.levelOrder(tree.root))
print(tree.isSymmetric(tree.root))
# print(tree.size_tree())

# print(tree.preorder_iterative(tree.root))
# print(tree.max_depth(tree.root))
# print(tree)