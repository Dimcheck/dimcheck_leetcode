"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def multiply(num1: str, num2: str) -> str:
    """
    Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"
    """
    if "0" in [num1, num2]:
        return '0'

    num1, num2 = num1[::-1], num2[::-1]
    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1)):
        for j in range(len(num2)):
            digit = int(num1[i]) * int(num2[j])

            result[i + j] += digit
            result[i + j + 1] += (result[i + j] // 10)
            result[i + j] = result[i + j] % 10

    result, start = result[::-1], 0
    while start < len(result) and result[start] == 0:
        start += 1

    result = map(str, result[start:])
    return ''.join(result)


print(multiply(num1 = "2", num2 = "3"))        #6
print(multiply(num1 = "123", num2 = "456"))    #56088