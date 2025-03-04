"""
Given two binary strings a and b, return their sum as a binary string.
"""

def addBinaryv1(a: str, b: str) -> str:
    """
        Example 1:
        Input: a = "11", b = "1"
        Output: "100"

        Example 2:
        Input: a = "1010", b = "1011"
        Output: "10101"
    """

    c = bin(int(a, 2) + int(b, 2))
    return c[2:]

def addBinaryv2(a: str, b: str) -> str:
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)

    carry = 0
    result = []

    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1

        if carry % 2 == 1:
            result.append('1')
        else:
            result.append('0')

        carry //= 2

    if carry == 1:
        result.append('1')

    return ''.join(result[::-1])





# print(addBinaryv2(a = "11", b = "1"))
# print(addBinaryv2(a = "1", b = "100"))
print(addBinaryv2(a = "1010", b = "1011"))