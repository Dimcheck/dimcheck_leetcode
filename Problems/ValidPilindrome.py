"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

def isPalindrome(s: str) -> bool:
    """
    Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
    """

    extracted_s = ''.join(filter(str.isalnum, s)).lower()
    return extracted_s == ''.join(reversed(extracted_s))


def isPalindromev2(s: str) -> bool:
    extracted_s = str(s)

    start = 0
    end = len(extracted_s) - 1

    while start < end:
        if extracted_s[start] != extracted_s[end]:
            return False
        elif extracted_s[start] == extracted_s[end]:
            start += 1
            end -= 1
    return True


isPalindromev2(s="A man, a plan, a canal: Panama")
isPalindromev2(s=-121)
# isPalindrome(s=" ")
# isPalindrome(s="plan, ")