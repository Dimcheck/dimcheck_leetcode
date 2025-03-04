from typing import Any


class Node:
    """
    Python lists aren’t really lists in the traditional computer science sense of the word, and that explains the puzzle
    of why append is so much more efficient than insert. A classical list—a so-called linked list—is implemented as
    a series of nodes, each (except for the last) keeping a reference to the next.
    """
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data) + str(self.next)

    def __str__(self) -> str:
        return str(self.data)


class SinglyLL:
    """
    To create Nodes:
        name_node = Node('a', Node('b', Node('o', Node('b', Node('a')))))
        second_node = Node('YO')

    To use LL:
        l2 = SinglyLL(name_node)
        l2.prepend(second_node)
        l2.head
        l2.head.next
        l2.insert_after_node(l2.head, 'Y')
    """
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def all_data(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def length(self):
        current = self.head
        count = 0

        while current:
            current = current.next
            count += 1
        return count

    def length_recursive(self, node: Node):
        """
        node: l.head
        """
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def append(self, data: Node | Any):
        """
        Push element to the end of LL.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return None

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data: Node | Any):
        """
        Push element before all elements in LL.
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev: Node, data: Node | Any):
        """
        Push element in specific place between nodes.
        """
        if not prev:
            print("There is no prev_node")
            return None

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def swap_node(self, node1: Node | Any, node2: Node | Any):
        if node1 == node2:
            return None

        prev_1 = None
        current_1 = self.head
        while current_1 and current_1.data != node1:
            prev_1 = current_1
            current_1 = current_1.next

        prev_2 = None
        current_2 = self.head
        while current_2 and current_2.data != node2:
            prev_2 = current_2
            current_2 = current_2.next

        if not current_1 or not current_2:
            return None

        if prev_1:
            prev_1.next = current_2
        else:
            self.head = current_2

        if prev_2:
            prev_2.next = current_1
        else:
            self.head = current_1

        current_1.next, current_2.next = current_2.next, current_1.next

    def delete_node(self, data: Node | Any):
        """
        Deletes an element with corresponded data in node.
        """
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return None

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return None

        prev.next = current.next
        current = None

    def delete_nodes_r(self, data: Node | Any):
        """
        Deletes all elements with corresponded data in node.
        """
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return self.delete_nodes_r(data)

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return None

        if current.data == data:
            self.head = current
            prev.next = current.next
            return self.delete_nodes_r(data)

    def delete_node_at(self, position: int):
        """
        Deletes an element in specific place.
        """
        current = self.head
        if position == 0:
            self.head == current.next
            current = None
            return None

        prev = None
        count = 1
        while current and count != position:
            prev = current
            current = current.next
            count += 1

        if current is None:
            return None

        prev.next = current.next
        current = None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_r(self, head: Node):
        def _reverse_r(current, prev):
            if not current:
                return prev

            next = current.next
            current.next = prev
            prev = current
            current = next
            return _reverse_r(current, prev)

        self.head = _reverse_r(current=self.head, prev=None)

    def merge_2_sorted_lists(self, l2: Node):
        p1 = self.head
        p2 = l2.head
        s = None

        if not p1:
            return p2
        if not p2:
            return p1

        if p1 and p2:
            if p1.data <= p2.data:
                s = p1
                p1 = s.next
            else:
                s = p2
                p2 = s.next

            new_head = s

        while p1 and p2:
            if p1.data <= p2.data:
                s.next = p1
                s = p1
                p1 = s.next
            else:
                s.next = p2
                s = p2
                p2 = s.next

        if not p1:
            s.next = p2
        if not p2:
            s.next = p1

        return new_head

    def remove_duplicates(self):
        current = self.head
        prev = None
        hashmap = {}

        while current:
            if current.data in hashmap:
                prev.next = current.next
                current = None
            else:
                hashmap[current.data] = 1
                prev = current
            current = prev.next

sl1 = Node(5, Node(8, Node(10, Node(12, Node(15)))))
sl2 = Node(2, Node(3, Node(6, Node(9, Node(11)))))

# name_node = Node('a', Node('b', Node('o', Node('b', Node('a')))))
example_node = Node('A', Node("B", Node('C', Node('D'))))


l1 = SinglyLL(sl1)
l2 = SinglyLL(sl2)
# l3 = SinglyLL(Node(1, Node(6, Node(1, Node(4, Node(2, Node(2)))))))
# l3 = SinglyLL(Node(1, Node(2, Node(6, Node(3, Node(4, Node(6, Node(5))))))))
l3 = SinglyLL(Node(1, Node(2, Node(6, Node(3)))))
# l3 = SinglyLL(Node(7, Node(7, Node(7, Node(7)))))
l3.all_data()
l3.delete_nodes_r(6)
l3.all_data()
# l3 = SinglyLL(Node(2, Node(3, Node(6, Node(3, Node(1, Node(1)))))))



