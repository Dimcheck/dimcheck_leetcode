"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

"""
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    valid_result = {}

    for initial_word in strs:
        sorted_word = ''.join(sorted(initial_word))

        if sorted_word not in valid_result:
            valid_result[sorted_word] = [initial_word]
        else:
            valid_result[sorted_word].append(initial_word)

    print(valid_result.values())

groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"])