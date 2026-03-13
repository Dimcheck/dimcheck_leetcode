"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
https://leetcode.com/problems/pascals-triangle/
"""

from typing import List


def generate(numRows: int) -> List[List[int]]:
    """
    Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    Example 2:
    Input: numRows = 1
    Output: [[1]]
    """
    rows = []
    while numRows != 0:
        rows.append([1])

        numRows -= 1

print(generate(numRows = 5))
print(generate(numRows = 1))


