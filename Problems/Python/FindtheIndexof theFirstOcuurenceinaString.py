"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""


def strStr(haystack: str, needle: str) -> int:
    """
    Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

    Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.
    """

    needle_length = len(needle)
    start = 0
    end = needle_length

    while end <= len(haystack):
        if haystack[start:end] == needle:
            return start

        start += needle_length
        end += needle_length
    return -1

def strStrv2(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1



print(strStrv2(haystack = "sadbutsad", needle = "sad"))
print(strStrv2(haystack="hello", needle="ll"))
print(strStrv2(haystack="mississippi", needle="issi"))