from typing import Any


class Node(object):
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.value)


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data: Any):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current: Node):
        if data < current.value:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(data, current.left)
        elif data > current.value:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(data, current.right)
        else:
            print('Value is already present in a tree')

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, current: Node):
        if data > current.value and current.right:
            return self._find(data, current.right)
        elif data < current.value and current.left:
            return self._find(data, current.left)
        if data == current.value:
            return True


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
print(bst.find(8))
