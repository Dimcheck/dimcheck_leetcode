"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


def isAnagramv1(s: str, t: str) -> bool:
    """
    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:

    Input: s = "rat", t = "car"
    Output: false
    """
    s, t = list(s), list(t)
    s.sort(), t.sort()

    print(s, t)

    if s == t:
        return True
    else:
        return False


def isAnagramv2(s: str, t: str) -> bool:
    """
    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:

    Input: s = "rat", t = "car"
    Output: false
    """
    return sorted(s) == sorted(t)

isAnagramv2(s="rat", t="car")
