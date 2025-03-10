"""Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal
substring
consisting of non-space characters only.
"""

def lengthOfLastWord(s: str) -> int:
    """
    Example 1:
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.

    Example 2:
    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.
    """

    return len(s.split()[-1])

# print(lengthOfLastWord(s = "   fly me   to   the moon  "))





