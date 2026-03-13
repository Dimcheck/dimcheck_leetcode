"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """
    Example 1:

    Input: nums = [1,2,3,1]
    Output: true

    Example 2:

    Input: nums = [1,2,3,4]
    Output: false
    """
    return False if len(nums) == len(set(nums)) else True

def containsDuplicatev2(nums: List[int]) -> bool:
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)

    return False


print(containsDuplicate(nums=[1, 2, 3, 1]))
print(containsDuplicatev2(nums=[1, 2, 3, 1]))
