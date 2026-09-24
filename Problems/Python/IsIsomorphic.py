"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:

    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:
Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
Input: s = "paper", t = "title"
Output: true
Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
"""


def isIsomorphic(s: str, t: str) -> bool:
    history, counter = {}, 0

    while counter < len(s):
        if not history.get(s[counter]) and t[counter] not in history.values():
            history[s[counter]] = t[counter]
        if history.get(s[counter]) != t[counter]:
            return False
        counter += 1
    return True



# print(isIsomorphic(s="egg", t="add"))       # true
# print(isIsomorphic(s="egg", t="adc"))       # false
# print(isIsomorphic(s="foo", t="bar"))       # false
# print(isIsomorphic(s="paper", t="titel"))       # true
# print(isIsomorphic(s="bbbaaaba", t="aaabbbba"))     # false
print(isIsomorphic(s="badc", t="baba"))     # false

