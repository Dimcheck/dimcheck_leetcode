'''
Given a string s, find the length of the longest
without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''


def lengthOfLongestSubstringv1(s: str) -> int:
    table_counter = 0
    substr_table = [[]]
    for c in s:
        if c not in substr_table[table_counter]:
            substr_table[table_counter].append(c)
        else:
            table_counter += 1
            substr_table.append([c])

    substr_table.sort(key=len, reverse=True)
    print(substr_table)
    return len(substr_table[0])


def lengthOfLongestSubstringv2(s: str) -> int:
    char_set = set()
    l, res = 0, 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)
    return res



lengthOfLongestSubstringv2('dvdf')
lengthOfLongestSubstringv2('bbbbb')
lengthOfLongestSubstringv2('abcabcbb')
lengthOfLongestSubstringv2('pwwkew')
