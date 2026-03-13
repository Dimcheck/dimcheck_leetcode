'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''


def reverse(x: int) -> int:
    str_view = str(x)[::-1]
    if str_view[-1] == '-':
        str_view = '-' + str_view[:-1]

    res = int(str_view)
    if res < -2147483648 or res > 2147483647:
        return 0
    return res




print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))

