"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import List, Optional


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def addTwoNumbers(l1: Optional[List], l2: Optional[List]) -> Optional[List]:
    """
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    """
    l1, l2 = l1[::-1], l2[::-1]
    f_n = int(''.join(map(str, l1)))
    s_n = int(''.join(map(str, l2)))

    return f_n + s_n



addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4])
