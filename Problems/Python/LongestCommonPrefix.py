"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
from typing import List


def longestCommonPrefixv1(strs: List[str]) -> str:
    """
    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    """
    counter = 0
    prefix = ''

    if len(strs) <= 1:
        return strs[0]

    while strs:
        try:
            if strs[0][:counter] == strs[1][:counter] and strs[0][:counter] == strs[2][:counter]:
                prefix = strs[0][:counter]
                counter += 1
            else:
                break
        except IndexError:
            break
    return prefix

def longestCommonPrefixv2(strs: List[str]) -> str:
    if not strs:
        return ""

    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str





longestCommonPrefixv2(["flower","flow","flight"])
longestCommonPrefixv2(["ab","a",])
# longestCommonPrefix(["dog"])