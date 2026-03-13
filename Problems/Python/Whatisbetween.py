"""
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.
"""


def between(a, b):
    """
    For example:
    a = 1
    b = 4
    --> [1, 2, 3, 4]
    """
    result = []
    while a <= b:
        result.append(a)
        a += 1

    return result

def betweenv2(a, b):
    """
    For example:
    a = 1
    b = 4
    --> [1, 2, 3, 4]
    """
    return list(range(a, b+1))


betweenv2(a=1, b=4)
