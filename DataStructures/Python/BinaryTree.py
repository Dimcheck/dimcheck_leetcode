class BinaryTree:
    """
    Use:
    new_tree = BinaryTree.from_values((0, 1))
    tree = BinaryTree(BinaryTree('a', 'b'), BinaryTree('c', 'd'))

    new_tree
    new_tree.right
    new_tree.right.left
    """

    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + str(self.right)

    @classmethod
    def from_values(cls, values: tuple):
        left, right = values[0], values[1]
        return cls(cls(left, right), cls(left, right))

new_tree = BinaryTree.from_values((0, 1))
print(new_tree)


