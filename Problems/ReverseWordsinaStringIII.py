"""
Given a string s, reverse the order of characters in each word within a sentence while
still preserving whitespace and initial word order.
"""

def reverseWords(s: str) -> str:
    """
    Example 1:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    Example 2:
    Input: s = "God Ding"
    Output: "doG gniD"
    """

    new_sl = [s[::-1] for s in s.split(' ')]
    s = ' '.join(new_sl)
    return s


print(reverseWords(s="Let's take LeetCode contest"))